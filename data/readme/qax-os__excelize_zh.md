<p align="center"><img width="650" src="./excelize.svg" alt="Excelize logo"></p>

<p align="center">
    <a href="https://github.com/xuri/excelize/actions/workflows/go.yml"><img src="https://github.com/xuri/excelize/actions/workflows/go.yml/badge.svg" alt="Build Status"></a>
    <a href="https://codecov.io/gh/qax-os/excelize"><img src="https://codecov.io/gh/qax-os/excelize/branch/master/graph/badge.svg" alt="Code Coverage"></a>
    <a href="https://goreportcard.com/report/github.com/xuri/excelize/v2"><img src="https://img.shields.io/badge/go.dev-reference-007d9c?logo=go&logoColor=white" alt="Go Report Card"></a>
    <a href="https://pkg.go.dev/github.com/xuri/excelize/v2"><img src="https://img.shields.io/badge/license-bsd-orange.svg" alt="Licenses"></a>
    <a href="https://www.paypal.com/paypalme/xuri"><img src="https://img.shields.io/badge/Donate-PayPal-green.svg" alt="Donate"></a>
</p>

# Excelize

## 简介

Excelize 是一个使用纯 Go 语言编写的库，提供了一组函数，允许你读写 XLAM / XLSM / XLSX / XLTM / XLTX 文件。支持读取和写入由 Microsoft Excel&trade; 2007 及更高版本生成的电子表格文档。该库具有高度兼容性，支持复杂组件，并提供流式 API（streaming API）用于生成或从包含海量数据的工作表中读取数据。本库需要 Go 1.25.0 或更高版本。完整文档可通过 Go 内置的文档工具查看，也可在线访问 [go.dev](https://pkg.go.dev/github.com/xuri/excelize/v2) 和[文档参考](https://xuri.me/excelize/)。

## 基本用法

### 安装

```bash
go get github.com/xuri/excelize
```

- 如果你的包使用 [Go Modules](https://go.dev/blog/using-go-modules) 进行管理，请使用以下命令进行安装。

```bash
go get github.com/xuri/excelize/v2
```

### 创建电子表格

以下是创建一个电子表格文件的最小化示例用法。

```go
package main

import (
    "fmt"

    "github.com/xuri/excelize/v2"
)

func main() {
    f := excelize.NewFile()
    defer func() {
        if err := f.Close(); err != nil {
            fmt.Println(err)
        }
    }()
    // Create a new sheet.
    index, err := f.NewSheet("Sheet2")
    if err != nil {
        fmt.Println(err)
        return
    }
    // Set value of a cell.
    f.SetCellValue("Sheet2", "A2", "Hello world.")
    f.SetCellValue("Sheet1", "B2", 100)
    // Set active sheet of the workbook.
    f.SetActiveSheet(index)
    // Save spreadsheet by the given path.
    if err := f.SaveAs("Book1.xlsx"); err != nil {
        fmt.Println(err)
    }
}
```

### 读取电子表格

以下是读取电子表格文档的基础示例。

```go
package main

import (
    "fmt"

    "github.com/xuri/excelize/v2"
)

func main() {
    f, err := excelize.OpenFile("Book1.xlsx")
    if err != nil {
        fmt.Println(err)
        return
    }
    defer func() {
        // Close the spreadsheet.
        if err := f.Close(); err != nil {
            fmt.Println(err)
        }
    }()
    // Get value from cell by given worksheet name and cell reference.
    cell, err := f.GetCellValue("Sheet1", "B2")
    if err != nil {
        fmt.Println(err)
        return
    }
    fmt.Println(cell)
    // Get all the rows in the Sheet1.
    rows, err := f.GetRows("Sheet1")
    if err != nil {
        fmt.Println(err)
        return
    }
    for _, row := range rows {
        for _, colCell := range row {
            fmt.Print(colCell, "\t")
        }
        fmt.Println()
    }
}
```

### 向电子表格文件添加图表

使用 Excelize，图表的生成和管理只需几行代码即可完成。你可以基于工作表中的数据构建图表，或者完全不依赖数据直接生成图表。

<p align="center"><img width="650" src="./test/images/chart.png" alt="Excelize"></p>

```go
package main

import (
    "fmt"

    "github.com/xuri/excelize/v2"
)

func main() {
    f := excelize.NewFile()
    defer func() {
        if err := f.Close(); err != nil {
            fmt.Println(err)
        }
    }()
    for idx, row := range [][]interface{}{
        {nil, "Apple", "Orange", "Pear"}, {"Small", 2, 3, 3},
        {"Normal", 5, 2, 4}, {"Large", 6, 7, 8},
    } {
        cell, err := excelize.CoordinatesToCellName(1, idx+1)
        if err != nil {
            fmt.Println(err)
            return
        }
        f.SetSheetRow("Sheet1", cell, &row)
    }
    if err := f.AddChart("Sheet1", "E1", &excelize.Chart{
        Type: excelize.Col3DClustered,
        Series: []excelize.ChartSeries{
            {
                Name:       "Sheet1!$A$2",
                Categories: "Sheet1!$B$1:$D$1",
                Values:     "Sheet1!$B$2:$D$2",
            },
            {
                Name:       "Sheet1!$A$3",
                Categories: "Sheet1!$B$1:$D$1",
                Values:     "Sheet1!$B$3:$D$3",
            },
            {
                Name:       "Sheet1!$A$4",
                Categories: "Sheet1!$B$1:$D$1",
                Values:     "Sheet1!$B$4:$D$4",
            }},
        Title: excelize.ChartTitle{
            Paragraph: []excelize.RichTextRun{
                {
                    Text: "Fruit 3D Clustered Column Chart",
                },
            },
        },
    }); err != nil {
        fmt.Println(err)
        return
    }
    // Save spreadsheet by the given path.
    if err := f.SaveAs("Book1.xlsx"); err != nil {
        fmt.Println(err)
    }
}
```

### 向电子表格文件添加图片

```go
package main

import (
    "fmt"
    _ "image/gif"
    _ "image/jpeg"
    _ "image/png"

    "github.com/xuri/excelize/v2"
)

func main() {
    f, err := excelize.OpenFile("Book1.xlsx")
    if err != nil {
        fmt.Println(err)
        return
    }
    defer func() {
        // Close the spreadsheet.
        if err := f.Close(); err != nil {
            fmt.Println(err)
        }
    }()
    // Insert a picture.
    if err := f.AddPicture("Sheet1", "A2", "image.png", nil); err != nil {
        fmt.Println(err)
    }
    // Insert a picture to worksheet with scaling.
    if err := f.AddPicture("Sheet1", "D2", "image.jpg",
        &excelize.GraphicOptions{ScaleX: 0.5, ScaleY: 0.5}); err != nil {
        fmt.Println(err)
    }
    // Insert a picture offset in the cell with printing support.
    enable, disable := true, false
    if err := f.AddPicture("Sheet1", "H2", "image.gif",
        &excelize.GraphicOptions{
            PrintObject:     &enable,
            LockAspectRatio: false,
            OffsetX:         15,
            OffsetY:         10,
            Locked:          &disable,
        }); err != nil {
        fmt.Println(err)
    }
    // Save the spreadsheet with the origin path.
    if err = f.Save(); err != nil {
        fmt.Println(err)
    }
}
```

## 贡献代码

欢迎贡献代码！请提交 Pull Request 以修复 Bug，或创建 Issue 讨论新功能与变更。XML 格式符合 [ECMA-376 Office Open XML 标准第 5 版第一部分](https://www.ecma-international.org/publications-and-standards/standards/ecma-376/)。

## 许可证

本程序遵循 BSD 3-Clause 许可证条款。详见 [https://opensource.org/licenses/BSD-3-Clause](https://opensource.org/licenses/BSD-3-Clause)。

Excel 标志是 [Microsoft Corporation](https://aka.ms/trademarks-usage) 的商标。本图示为改编作品。

Go 海象（gopher）由 [Renee French](https://go.dev/doc/gopher/README) 创作。依据 [知识共享署名 4.0 许可证](http://creativecommons.org/licenses/by/4.0/) 发布。

## 金牌赞助商

<a href="https://www.gravityclimate.com" alt="Gravity"><img width="120" src="https://xuri.me/excelize/images/vendor/gravityclimate.com.svg" alt="Gravity"></a>