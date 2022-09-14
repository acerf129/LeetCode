using System;
using System.Collections.ObjectModel;
using System.Collections.Generic;
public class Program{
    public static void Main(){
        var arr= new List{20,40,35,85,70};
        var collection=new Collection(arr);
        arr.Add(60);
        arr.Sort();
        Console.WriteLine(String.Join(",",collection));
    }
}