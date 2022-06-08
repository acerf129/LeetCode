public interface ITableReader{
    string GetCell(int col,int row);
}
public class XlsTableReader:ITableReader{
    public string GetCell(int col,int row){
        //Interop.Excel 
    }
}
public class XlsxTableReader:ITableReader{
    public string GetCell(int col,int row){
        //Document.OpenXml
    }
}
public class CsvReader:ITableReader{
    public string GetCell(int col,int row){
        //string.split
    }
}
public class MyExcelParser{
    private ITableReader tableReader;
    public MyExcelParser(ITableReader _tableReader){
        this.tableReader=_tableReader;
    }
    public void Parser(int col,int row){
        string name=tableReader.GetCell(col,row);
    }
}
public class Program{
    static void Main(string []args){
        MyExcelParser excelParser= new MyExcelParser(new XlsTableReader());
    }
}