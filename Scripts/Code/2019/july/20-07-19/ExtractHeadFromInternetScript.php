<?php
ini_set('xdebug.var_display_max_depth', -1);
ini_set('xdebug.var_display_max_children', -1);
ini_set('xdebug.var_display_max_data', -1);
set_time_limit(0);

$host = "host = 127.0.0.1";
$port = "port = 5432";
$db = "dbname = gsm_new";
$credentials = "user=postgres password=postgres";

$conn = pg_connect("$host $port $db $credentials");
if(!$conn)
{
  echo pg_last_error();
}
$link_arr = array(
              "https://www.gsmarena.com/blu-phones-67.php",
              "https://www.gsmarena.com/plum-phones-72.php",
              "https://www.gsmarena.com/apple-phones-48.php",
              "https://www.gsmarena.com/google-phones-107.php",
              "https://www.gsmarena.com/alcatel-phones-5.php",
              "https://www.gsmarena.com/acer-phones-59.php",
              "https://www.gsmarena.com/huawei-phones-58.php",
              "https://www.gsmarena.com/honor-phones-121.php",
              "https://www.gsmarena.com/zte-phones-62.php",
              "https://www.gsmarena.com/infinix-phones-119.php",
              "https://www.gsmarena.com/oppo-phones-82.php",
              "https://www.gsmarena.com/microsoft-phones-64.php",
              "https://www.gsmarena.com/tecno-phones-120.php",
              "https://www.gsmarena.com/sony-phones-7.php",
              "https://www.gsmarena.com/realme-phones-118.php",
              "https://www.gsmarena.com/vodafone-phones-53.php",
              "https://www.gsmarena.com/wiko-phones-96.php",
              "https://www.gsmarena.com/lg-phones-20.php",
              "https://www.gsmarena.com/oneplus-phones-95.php",
              "https://www.gsmarena.com/energizer-phones-106.php",
              "https://www.gsmarena.com/panasonic-phones-6.php",
              "https://www.gsmarena.com/htc-phones-45.php",
              "https://www.gsmarena.com/vivo-phones-98.php",
              "https://www.gsmarena.com/cat-phones-89.php",
              "https://www.gsmarena.com/yu-phones-100.php",
              "https://www.gsmarena.com/meizu-phones-74.php",
              "https://www.gsmarena.com/sharp-phones-23.php",
              "https://www.gsmarena.com/verykool-phones-70.php",
              "https://www.gsmarena.com/lenovo-phones-73.php",
              "https://www.gsmarena.com/blackberry-phones-36.php",
              "https://www.gsmarena.com/micromax-phones-66.php",
              "https://www.gsmarena.com/samsung-phones-9.php",
              "https://www.gsmarena.com/nokia-phones-1.php",
              "https://www.gsmarena.com/lava-phones-94.php",
              "https://www.gsmarena.com/xiaomi-phones-80.php",
              "https://www.gsmarena.com/asus-phones-46.php",
              "https://www.gsmarena.com/motorola-phones-4.php"
  );
$product_arr_done = array();
foreach($link_arr as $link1)
{
  var_dump($link1);
  $html1 = file_get_contents($link1);
  libxml_use_internal_errors(TRUE);

  if($html1)
  {
    $arrlink1 = array();
    $arrlink1[] =$link1;
    $body1 = new DOMDocument();
    $body1->loadHTML($html1);
    libxml_clear_errors();

    $path1 = new DOMXPath($body1);
    $all1 = $path1->query('//div[@class="nav-pages"]/a');
    foreach($all1 as $all)
    {
      $arrlink1[]='https://www.gsmarena.com/'.$all->getAttribute('href');
    }
    var_dump($arrlink1);
    foreach($arrlink1 as $all)
    { 
      $link2 = $all;
      $html2 = file_get_contents($link2);
      $body2 = new DOMDocument();
      $body2->loadHTML($html2);
      $path2 = new DOMXPath($body2);
      $all2 = $path2->query('//div[@class="makers"]/ul/li/a');
      foreach($all2 as $all)
      {
        $dataObj= json_decode('{}');
        $pagelink ='https://www.gsmarena.com/'.$all->getAttribute('href');
        var_dump($pagelink);
        $html3 = file_get_contents($pagelink);

        $body3 = new DOMDocument();
        $body3->loadHTML($html3);
        $path3= new DOMXPath($body3);

        $all3 = $path3->query('//h1[@class="specs-phone-name-title"]');
        foreach($all3 as $all)
        {

          $name=pg_escape_string($conn,$all->nodeValue);
          $dataObj->name=$name;
        }
        $findName = "SELECT Name from public.home_allpro where name ilike '$name'";
        $result = (pg_query($conn,$findName));
        $duplicate = false;
        while ($row = pg_fetch_row($result)) {
          if(strtolower($row[0]) == strtolower($name)){
            $duplicate = true;
          }
        }
        if($duplicate == false || in_array($name, $product_arr_done)){
          continue;
        }
        array_push($product_arr_done,$name);
        
        $all3 = $path3->query('//span[@data-spec="released-hl"]');
        foreach($all3 as $all)
        {

          $date=pg_escape_string($conn,$all->nodeValue);
          $dataObj->date=$date;

        }
        $all4 = $path3->query('//span[@data-spec="body-hl"]');
        foreach($all4 as $all)
        {

          $body=pg_escape_string($conn,$all->nodeValue);
          $dataObj->body=$body;

        }
        $all5 = $path3->query('//span[@data-spec="os-hl"]');
        foreach($all5 as $all)
        {
          $os=pg_escape_string($conn,$all->nodeValue);
          $dataObj->os=$os;
        }
        $all6 = $path3->query('//span[@data-spec="storage-hl"]');
        foreach($all6 as $all)
        {
          $storage=pg_escape_string($conn,$all->nodeValue);
          $dataObj->storage=$storage;
        }
        $all7 = $path3->query('//span[@data-spec="displaysize-hl"]');
        foreach($all7 as $all)
        {
          $display=pg_escape_string($conn,$all->nodeValue);
          $dataObj->display=$display;
        }
        $all8 = $path3->query('//div[@data-spec="displayres-hl"]');
        foreach($all8 as $all)
        {
          $resolution=pg_escape_string($conn,$all->nodeValue);
          $dataObj->resolution=$resolution;
        }
        $all9 = $path3->query('//span[@data-spec="camerapixels-hl"]');
        foreach($all9 as $all)
        {
          $main_camera=pg_escape_string($conn,$all->nodeValue);
          $dataObj->main_camera=$main_camera;
        }
        $all10 = $path3->query('//div[@data-spec="videopixels-hl"]');
        foreach($all10 as $all)
        {
          $video_pixel=pg_escape_string($conn,$all->nodeValue);
          $dataObj->video_pixel=$video_pixel;
        }
        $all11 = $path3->query('//span[@data-spec="ramsize-hl"]');
        foreach($all11 as $all)
        {
          $ram=pg_escape_string($conn,$all->nodeValue);
          $dataObj->ram=$ram;
        }
        $all12 = $path3->query('//div[@data-spec="chipset-hl"]');
        foreach($all12 as $all)
        {
          $processor=pg_escape_string($conn,$all->nodeValue);
          $dataObj->processor=$processor;
        }

        $all13 = $path3->query('//span[@data-spec="batsize-hl"]');
        foreach($all13 as $all)
        {
          $battery=pg_escape_string($conn,$all->nodeValue);
          $dataObj->battery=$battery;
        }
        $all14 = $path3->query('//div[@data-spec="battype-hl"]');
        foreach($all14 as $all)
        {
          $battery_type=pg_escape_string($conn,$all->nodeValue);
          $dataObj->battery_type=$battery_type;
        }
        $fobj = pg_escape_string($conn,json_encode($dataObj));
        var_dump($fobj);
        var_dump($name);
        $query = "update  public.home_allpro set head ='$fobj' where name = '$name'";
        var_dump($query);
        if(pg_query($conn,$query))
        {
          echo "done";
        }
        else
        {
          echo pg_last_error($conn);
        }
      }
      // var_dump($pagelink);
    }
  }
}



?>
