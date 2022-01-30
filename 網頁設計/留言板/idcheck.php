<?
$SQLStr = "SELECT* FROM message WHERE m_id='$m_id' AND m_pass='$pass'";
$res = db_query($SQLStr);
if(!(db_num_rows($res)>0))
{
echo"<script>"
echo"alert(\"密碼錯誤\");";
echo"location.herf = \"message_show.php?m_id=".$m_id."\";";
echo"</script>";
@break;



}