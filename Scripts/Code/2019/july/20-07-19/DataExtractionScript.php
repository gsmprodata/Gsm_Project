<?php
ini_set('xdebug.var_display_max_depth', -1);
ini_set('xdebug.var_display_max_children', -1);
ini_set('xdebug.var_display_max_data', -1);
set_time_limit(0);

function generateText($toMatch, $data, $conn) {
  $tables = $data->query('//div[@id="specs-list"]/table');
  $headingArr ="";
  $heading ="";
  $value = "";
  $item ="";
  $query= "";
  $i = 1;
  foreach($tables as $table){
  
    $headingArr = $data->query('//div[@id="specs-list"]/table['.$i.']/tr/th');
    $description = $data->query('//div[@id="specs-list"]/table['.$i.']/tr/td');
    $i++;
    foreach($headingArr as $all)
    {
      $heading = pg_escape_string($conn,$all->nodeValue);
    }
    if(strtolower($toMatch) == strtolower($heading)){
      foreach($description as $all)
      {
        $value =pg_escape_string($conn, $all->nodeValue);
        $item=$item.'!@#'.$value;
      }
      break;
    }else{
      continue;
    }
  }
  return str_replace(array("\r\n", "\r", "\n", "\t"), ' ', $item);
}

$host = "host = 127.0.0.1";
$port = "port = 5432";
$db = "dbname = GSM";
$credentials = "user=postgres password=postgres@123";

$conn = pg_connect("$host $port $db $credentials");
if(!$conn)
{
  echo pg_last_error();
}


    $link1 = "https://www.gsmarena.com/samsung-phones-9.php";

    $html1 = file_get_contents($link1);
    libxml_use_internal_errors(TRUE);

    if($html1)
    {
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
      // die;
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
          }
          // var_dump($name);
          $a=explode(' ',$name);
          $brand = $a[0];
          $findName = "SELECT Name from public.home_allpro where name ilike '$name'";
          $result = (pg_query($conn,$findName));
          $duplicate = false;
          while ($row = pg_fetch_row($result)) {
            if(strtolower($row[0]) == strtolower($name)){
              $duplicate = true;
              continue;
            };
          }
          if($duplicate == true){
            continue;
          }
          $network = "";
          $launch = "";
          $body = "";
          $display = "";
          $platform = "";
          $memory = "";
          $maincamera = "";
          $selfiecamera = "";
          $sound = "";
          $comms = "";
          $features = "";
          $battery = "";
          $misc = "";
          //inserting right value......
          $network = generateText("NETWORK", $path3, $conn);
          $launch = generateText("LAUNCH", $path3, $conn);
          $body = generateText("BODY", $path3, $conn);
          $display = generateText("DISPLAY", $path3, $conn);
          $platform = generateText("PLATFORM", $path3, $conn);
          $memory = generateText("MEMORY", $path3, $conn);
          $maincamera = generateText("MAIN CAMERA", $path3, $conn);
          $selfiecamera = generateText("SELFIE CAMERA", $path3, $conn);
          $sound = generateText("SOUND", $path3, $conn);
          $comms = generateText("COMMS", $path3, $conn);
          $features = generateText("FEATURES", $path3, $conn);
          $battery = generateText("BATTERY", $path3, $conn);
          $misc = generateText("MISC", $path3, $conn);

          $all3 = $path3->query('//div[@class="specs-photo-main"]/a/img');
          foreach($all3 as $all)
          {
            $img = pg_escape_string($conn,$all->getAttribute('src'));

          }
          $z = preg_replace("/\s/","_",$name);
          $zz = pg_escape_string($conn,$z).'.jpg';
          $loc = "imgfiles/$z.jpg";
          file_put_contents($loc, file_get_contents($img));
          $insert = "INSERT INTO public.home_allpro(
        name, brand, image_link, network, launch, body, display, platform, memory, main_camera, selfie_camera, sound, comms, features, battery, misc,img_name)
        VALUES ( '$name','$brand','$img','$network','$launch','$body','$display','$platform','$memory','$maincamera','$selfiecamera','$sound','$comms','$features','$battery','$misc','$zz')";
        if(pg_query($conn,$insert))
        {
          echo "entered";
          // die;
        }
        else
        {
          echo pg_last_error($conn);
        }
        //die;

        }
        // var_dump($pagelink);

      }
      echo "end please search for new brand";
    }



?>