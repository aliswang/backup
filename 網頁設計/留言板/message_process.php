


<?php
include("db_conn.php");
include("db_func.php");
$check=$_GET["check"];
$title=$_POST['title'];
$user=$_POST['user'];
$pass=$_POST["pass"];
$email=$_POST["email"];
$content=$_POST["content"];
$id=db_num_rows($res)+1;
function ChangWord($NewWord){
	
	$NewWord=str_replace("\r\n","<br>",$NewWord);
	

	
	$NewWord=ereg_replace("[']+","`",$NewWord);
	return $NewWord;
}

$time = date("Y-m-d g:i:s");
$ip= $_SERVER["REMOTE_ADDR"];


if ($check=="add")
{
$SQLSt = "INSERT INTO message (m_title,m_content,m_time,m_user,m_mail,m_ip,m_pass) Values('".$title."','".$content."','".$time."','".$user."','".$email."','".$ip."','".$pass."')";
echo $SQLSt;
//$SQLSt = "INSERT INTO message Values('111','111','111','1111_11_11_11_11_11','111','111','111','1111')";
	//$SQLStr2 = "INSERT INTO message Values('m_id','m_title','m_content',m_time,m_user,m_mail,m_ip,m_pass)";
	//$SQLStr.= "VALUES('$title','" .ChangWord($content) . "','$time','$user','$email','$pass','$ip')";
	$message=   "finish!";
	mysql_query($SQLSt);
}
if($check=="upd")
{include("idcheck.php");
$SQLStr = "UPDATA  message SET m_title='$title', m_content='".ChangWord($countent).",m_time='$m_time',";
	$SQLStr.="m_mail='$mail',m_ip='$ip' WHERE m_id ='$m_id'";
	$message=   " finish!";
	

	
}
if($check=="del")
{
	include("idcheck.php");
$SQLStr = "DELETE FROM MESSAGE WHERE M_ID = $M_IH";
	
	$message=   " 完成";
	

	
}

	
	//db_query($SQLStr);
?>



	<script>
alert("<?php echo $message; ?>");
location.href = "message_list.php?p=0";
</script>


