<?php
include("db_conn.php");
include("db_func.php");
$m_id=$_GET["m_id"];
$SQLStr = "SELECT* FROM message WHERE m_id='$m_id'";
//$SQLStr = "SELECT * FROM message ORDER BY m_time DESC";
$row = db_query("$SQLStr");
$res = db_fetch_array($row);
?>


<script>
fuction update()
{
	var pass1 = document.form1.pass.value;
	var m_id1 = document.form1.mid.value;
	window.open("message_update.php?m_id="+m_id1+"&pass="+pass1,"update","width=640,height=480,status=0,scrollbars=0,resizable=1,menubar=0,toolbar=0,location=0");
}
</script>


<form name="form1" method= "post" action="messge_process.php?check=del">
<table width="550" align="center" cellpadding="1"  cellspacing="1" border="1">
<tr>
<table width="549" align="center" cellpadding="0"  cellspacing="0" border="1">
<tr>
<td bgcolor="#FFFFFF" align="center">
<a href="message_reply.php?m_id=<?php=$m_id?>">回復</a>
</td>
<td  colspan="3"  bgcolor="#CCCCCC" align="center">
<b><font size="4">內容</font></b>
</td>
</tr>
<tr>
<td bgcolor="#99CCFF" align="center">聯絡人</td>
<td colspan="3" align="center">
<a href="<?php=$res['m_mail']?>"><?php=$res['m_user']?></a> //???
</td>
</tr>
<tr>
<td bgcolor="#CC9999" align="center" height="21">主題</td>
<td bgcolor="#FFFFFF" align="center"  colspan="3" height="21">
<?php
echo $res['m_title'];
?>
</td>
</tr>
<tr bgcolor="#FFCCCC">
<td colspan="4" align="center">
SHOW內容
</td>
</tr>
<tr>
<td colspan="4" align="centeer">
<?php
echo $res['m_content'];
?>
</td>
</tr>
<tr>
<td bgcolor="#99CCCC" align="center" >日期</td>
<td bgcolor="#FFFFFFFF" align="center" >
<?php echo $res['m_time'];?>
</td>
<td bgcolor="#99CCCC" align="center" >FROM</td>
<td bgcolor="#FFFFFFFF" align="center" >
<?php echo $res['m_ip'];?>
</td>
</tr>
<tr>
<td bgcolor="#99CCFF" align="center"  colspan="4">
<input type="button" name="Submit1" value="修改" onClick="update();">
<input type="submit" name="Submit" value="刪除留言">
<input type="password" name="pass" size="10">
<input type="hidden" name="m_id" value="<?=$m_id?>">
<font color="#FF0000"></font>
</tr>
</table>
</td>
</tr>
</table>
</form>














































































