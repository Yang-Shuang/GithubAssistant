# [supertest](https://forwardemail.github.io/superagent/)

[![build status](https://github.com/forwardemail/supertest/actions/workflows/ci.yml/badge.svg)](https://github.com/forwardemail/supertest/actions/workflows/ci.yml)
[![code coverage](https://img.shields.io/codecov/c/github/ladjs/supertest.svg)](https://codecov.io/gh/ladjs/supertest)
[![code style](https://img.shields.io/badge/code_style-XO-5ed9c7.svg)](https://github.com/sindresorhus/xo)
[![styled with prettier](https://img.shields.io/badge/styled_with-prettier-ff69b4.svg)](https://github.com/prettier/prettier)
[![made with lass](https://img.shields.io/badge/made_with-lass-95CC28.svg)](https://lass.js.org)
[![license](https://img.shields.io/github/license/ladjs/supertest.svg)](LICENSE)

> 通过 [superagent](http://github.com/ladjs/superagent) 轻松实现 HTTP 断言。由 [Forward Email](https://github.com/forwardemail) 和 [Lad](https://github.com/ladjs) 维护。

## 简介

本模块的初衷是提供一个用于测试 HTTP 的高级抽象层，同时仍允许你降级使用 [superagent](https://forwardemail.github.io/superagent/) 提供的[底层 API](https://forwardemail.github.io/superagent/)。

## 安装与使用

将 supertest 作为 npm 模块安装，并将其保存为开发依赖项写入你的 `package.json` 文件中：

```bash
npm install supertest --save-dev
```

  安装完成后，只需调用 ```require('supertest');``` 即可引用它。

## 示例

你可以向 `request()` 传递一个 `http.Server` 或 `Function`。如果服务器尚未监听连接，它会自动绑定到一个临时端口（ephemeral port），因此你无需手动管理端口号。

supertest 兼容任何测试框架。以下是一个完全不使用测试框架的示例：

```js
const request = require('supertest');
const express = require('express');

const app = express();

app.get('/user', function(req, res) {
  res.status(200).json({ name: 'john' });
});

request(app)
  .get('/user')
  .expect('Content-Type', /json/)
  .expect('Content-Length', '15')
  .expect(200)
  .end(function(err, res) {
    if (err) throw err;
  });
```

要启用 HTTP/2 协议，只需向 `request` 或 `request.agent` 附加一个选项即可：

```js
const request = require('supertest');
const express = require('express');

const app = express();

app.get('/user', function(req, res) {
  res.status(200).json({ name: 'john' });
});

request(app, { http2: true })
  .get('/user')
  .expect('Content-Type', /json/)
  .expect('Content-Length', '15')
  .expect(200)
  .end(function(err, res) {
    if (err) throw err;
  });

request.agent(app, { http2: true })
  .get('/user')
  .expect('Content-Type', /json/)
  .expect('Content-Length', '15')
  .expect(200)
  .end(function(err, res) {
    if (err) throw err;
  });
```

以下是使用 mocha 的示例，注意你可以直接将 `done` 传递给任意 `.expect()` 调用：

```js
describe('GET /user', function() {
  it('responds with json', function(done) {
    request(app)
      .get('/user')
      .set('Accept', 'application/json')
      .expect('Content-Type', /json/)
      .expect(200, done);
  });
});
```

你可以使用 `auth` 方法以与 [superagent](https://forwardemail.github.io/superagent/#authentication) 相同的方式传递 HTTP 用户名和密码：

```js
describe('GET /user', function() {
  it('responds with json', function(done) {
    request(app)
      .get('/user')
      .auth('username', 'password')
      .set('Accept', 'application/json')
      .expect('Content-Type', /json/)
      .expect(200, done);
  });
});
```

需要注意的是，如果你未添加状态码断言（例如 `.expect(302)`），superagent 现在会将任何 HTTP 错误（非 2XX 响应代码）作为第一个参数传递给回调函数。

如果你使用 `.end()` 方法，失败的 `.expect()` 断言不会抛出异常——它们会将错误作为参数返回给 `.end()` 回调。为了使测试用例失败，你需要重新抛出该错误或将其传递给 `done()`，如下所示：

```js
describe('POST /users', function() {
  it('responds with json', function(done) {
    request(app)
      .post('/users')
      .send({name: 'john'})
      .set('Accept', 'application/json')
      .expect('Content-Type', /json/)
      .expect(200)
      .end(function(err, res) {
        if (err) return done(err);
        return done();
      });
  });
});
```

你也可以使用 Promise：

```js
describe('GET /users', function() {
  it('responds with json', function() {
    return request(app)
      .get('/users')
      .set('Accept', 'application/json')
      .expect('Content-Type', /json/)
      .expect(200)
      .then(response => {
         expect(response.body.email).toEqual('foo@bar.com');
      })
  });
});
```

或使用 async/await 语法：

```js
describe('GET /users', function() {
  it('responds with json', async function() {
    const response = await request(app)
      .get('/users')
      .set('Accept', 'application/json')
    expect(response.headers["content-type"]).toMatch(/json/);
    expect(response.status).toEqual(200);
    expect(response.body.email).toEqual('foo@bar.com');
  });
});
```

断言会按照定义的顺序执行。利用这一特性，你可以在执行断言前修改响应体（body）或请求头（headers）。

```js
describe('POST /user', function() {
  it('user.name should be an case-insensitive match for "john"', function(done) {
    request(app)
      .post('/user')
      .send('name=john') // x-www-form-urlencoded upload
      .set('Accept', 'application/json')
      .expect(function(res) {
        res.body.id = 'some fixed id';
        res.body.name = res.body.name.toLowerCase();
      })
      .expect(200, {
        id: 'some fixed id',
        name: 'john'
      }, done);
  });
});
```

你能用 superagent 实现的功能，supertest 同样支持——例如多部分文件上传！

```js
request(app)
  .post('/')
  .field('name', 'my awesome avatar')
  .field('complex_object', '{"attribute": "value"}', {contentType: 'application/json'})
  .attach('avatar', 'test/fixtures/avatar.jpg')
  ...
```

每次传递 app 或 url 并非必要。如果你测试的是同一个主机，只需重新赋值初始化时的 app 或 url 即可，每次调用 `request.VERB()` 都会创建一个新的 `Test` 实例。

```js
request = request('http://localhost:5555');

request.get('/').expect(200, function(err){
  console.log(err);
});

request.get('/').expect('heya', function(err){
  console.log(err);
});
```

以下是一个使用 mocha 的示例，展示了如何持久化请求及其 Cookie：

```js
const request = require('supertest');
const should = require('should');
const express = require('express');
const cookieParser = require('cookie-parser');

describe('request.agent(app)', function() {
  const app = express();
  app.use(cookieParser());

  app.get('/', function(req, res) {
    res.cookie('cookie', 'hey');
    res.send();
  });

  app.get('/return', function(req, res) {
    if (req.cookies.cookie) res.send(req.cookies.cookie);
    else res.send(':(')
  });

  const agent = request.agent(app);

  it('should save cookies', function(done) {
    agent
    .get('/')
    .expect('set-cookie', 'cookie=hey; Path=/', done);
  });

  it('should send cookies', function(done) {
    agent
    .get('/return')
    .expect('hey', done);
  });
});
```

另一个示例由文件 [agency.js](https://github.com/ladjs/superagent/blob/master/test/node/agency.js) 引入：

以下是一个在请求中设置两个 Cookie 的示例。

```js
agent(app)
  .get('/api/content')
  .set('Cookie', ['nameOne=valueOne;nameTwo=valueTwo'])
  .send()
  .expect(200)
  .end((err, res) => {
    if (err) {
      return done(err);
    }
    expect(res.text).to.be.equal('hey');
    return done();
  });
```

## API

你可以使用任何 [superagent](http://github.com/ladjs/superagent) 的方法，包括 `.write()`、`.pipe()` 等，并在 `.end()` 回调中执行断言以满足底层需求。

### .expect(status[, fn])

断言响应 `status`（状态码）。

### .expect(status, body[, fn])

断言响应的 `status`（状态码）和 `body`（主体内容）。

### .expect(body[, fn])

使用字符串、正则表达式或已解析的响应体对象，断言响应的 `body` 文本。

### .expect(field, value[, fn])

使用字符串或正则表达式，断言请求头字段 `field` 的值 `value`。

### .expect(function(res) {})

传入自定义的断言函数。该函数会接收响应对象进行检查，如果检查失败则抛出错误。

```js
request(app)
  .get('/')
  .expect(hasPreviousAndNextKeys)
  .end(done);

function hasPreviousAndNextKeys(res) {
  if (!('next' in res.body)) throw new Error("missing next key");
  if (!('prev' in res.body)) throw new Error("missing prev key");
}
```

### .end(fn)

执行请求并调用 `fn(err, res)`。

## Cookie 处理

以下是使用 `set` 和 `not` Cookie 断言的示例：

```js
// setup super-test
const request = require('supertest');
const express = require('express');
const cookies = request.cookies;

// setup express test service
const app = express();

app.get('/users', function(req, res) {
  res.cookie('alpha', 'one', { domain: 'domain.com', path: '/', httpOnly: true });
  res.send(200, { name: 'tobi' });
});

// test request to service
request(app)
  .get('/users')
  .expect('Content-Type', /json/)
  .expect('Content-Length', '15')
  .expect(200)
  // assert 'alpha' cookie is set with domain, path, and httpOnly options
  .expect(cookies.set({ name: 'alpha', options: ['domain', 'path', 'httponly'] }))
  // assert 'bravo' cookie is NOT set
  .expect(cookies.not('set', { name: 'bravo' }))
  .end(function(err, res) {
    if (err) {
      throw err;
    }
  });
```

你也可以链式调用断言方法：

```js
cookies.set({/* ... */}).not('set', {/* ... */})
```

### Cookie 断言

函数和方法支持链式调用。

#### cookies([secret], [asserts])

获取用于 [super-test](https://github.com/visionmedia/supertest) `.expect()` 方法的断言函数。

*Arguments*

- `secret` - String or array of strings. Cookie signature secrets.
- `asserts(req, res)` - Function or array of functions. Failed custom assertions should throw.

#### .set(expects, [assert])

断言 Cookie 及其选项已设置。

*Arguments*

- `expects` - Object or array of objects.
  - `name` - String name of cookie.
  - `options` - *Optional* array of options.
- `assert` - *Optional* boolean "assert true" modifier. Default: `true`.

#### .reset(expects, [assert])

断言 Cookie 已设置，且此前已在请求头中存在过（用于验证刷新）。

*Arguments*

- `expects` - Object or array of objects.
  - `name` - String name of cookie.
- `assert` - *Optional* boolean "assert true" modifier. Default: `true`.

#### .new(expects, [assert])

断言 Cookie 已设置，且此前未在请求头中存在过（首次设置）。

*Arguments*

- `expects` - Object or array of objects.
  - `name` - String name of cookie.
- `assert` - *Optional* boolean "assert true" modifier. Default: `true`.

#### .renew(expects, [assert])

断言 Cookie 已设置，且其 `expires` 或 `max-age` 严格大于给定值。

*Arguments*

- `expects` - Object or array of objects.
  - `name` - String name of cookie.
  - `options` - Object of options. `use one of two options below`
  - `options`.`expires` - String UTC expiration for original cookie (in request headers).
  - `options`.`max-age` - Integer ttl in seconds for original cookie (in request headers).
- `assert` - *Optional* boolean "assert true" modifier. Default: `true`.

#### .contain(expects, [assert])

断言 Cookie 已设置，且包含指定的值和选项。如果 Cookie 是签名的，则需要先初始化 `cookies(secret)`。

*Arguments*

- `expects` - Object or array of objects.
  - `name` - String name of cookie.
  - `value` - *Optional* string unsigned value of cookie.
  - `options` - *Optional* object of options.
  - `options`.`domain` - *Optional* string domain.
  - `options`.`path` - *Optional* string path.
  - `options`.`expires` - *Optional* string UTC expiration.
  - `options`.`max-age` - *Optional* integer ttl, in seconds.
  - `options`.`secure` - *Optional* boolean secure flag.
  - `options`.`httponly` - *Optional* boolean httpOnly flag.
- `assert` - *Optional* boolean "assert true" modifier. Default: `true`.

#### .not(method, expects)

调用任意 Cookie 断言方法，并将“断言为真”修饰符设置为 `false`。语法糖。

*Arguments*

- `method` - String method name. Arguments of method name apply in `expects`.
- `expects` - Object or array of objects.
  - `name` - String name of cookie.
  - `value` - *Optional* string unsigned value of cookie.
  - `options` - *Optional* object of options.

## 说明

灵感来源于 [api-easy](https://github.com/flatiron/api-easy)，并移除了对 vows 的耦合。

## 许可证

MIT

[coverage-badge]: https://img.shields.io/codecov/c/github/ladjs/supertest.svg
[coverage]: https://codecov.io/gh/ladjs/supertest
[travis-badge]: https://travis-ci.org/ladjs/supertest.svg?branch=master
[travis]: https://travis-ci.org/ladjs/supertest
[dependencies-badge]: https://david-dm.org/ladjs/supertest/status.svg
[dependencies]: https://david-dm.org/ladjs/supertest
[prs-badge]: https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square
[prs]: http://makeapullrequest.com
[license-badge]: https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square
[license]: https://github.com/ladjs/supertest/blob/master/LICENSE