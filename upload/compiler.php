<?php
     $language = strtolower($_POST['language']);
     $code =$_POST['code'];

     $random = substr(md5(mt_rand()),0,7);
     $filepath="temp/" . $random . "." .$language;
     $programfile= fopen($filepath, "w");
     fwrite($programfile,$code);
     fclose($programfile);

     if($language == "cpp"){
         $outputExe=$random . ".exe";
         shell_exec("g++ $filepath -o $outputExe");
         $output= shell_exec ( __DIR__ . "\\$outputExe");
         echo $output;
      }  
?>