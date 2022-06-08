
 

public class Program{
public static async Task<JObject> GetJsonAsync(Uri uri)
{
    var jsonString = await client.GetStringAsync(uri);
    //var jsonString = await client.GetStringAsync(uri).ConfigureAwait(false);
    return JObject.Parse(jsonString);
}
}

 public class MyController : ApiController
{
  public string Get()
  {
    var jsonTask = GetJsonAsync("google.com");
    return jsonTask.Result.ToString();
  }
}
public class MyController : ApiController
{
  public Task<string> Get()
  {
    var json = await GetJsonAsync("google.com");
    return json.ToString();
  }
}