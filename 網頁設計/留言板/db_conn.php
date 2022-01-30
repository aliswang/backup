<?php
$db_host ="localhost:3307";
$db_login = "root";
$db_password ="root";
$db_name ="flag";
$conn = mysql_connect($db_host ,$db_login,$db_password);
if(!$conn){
	die("連線失敗");}
mysql_select_db($db_name);

?>







































