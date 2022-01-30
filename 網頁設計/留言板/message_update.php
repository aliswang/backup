<?

include("db_conn.php");
include("db_func.php");
$SQLStr = "SELECT* FROM message WHERE m_id='$m_id'";
$res = db_query("$SQLStr");
$row = db_fetch_array($res);

?>

<!------------------------------------------------------------->
<from name="form1" method="post" action="message_process.php?check=upd">
<table witdth="481" broder="1" cellpadding="0" cellspacing="0" align="center">
<tr>
<td>
<table witdth="480" broder="0"  brodercolor="#000099"  align="center">
<tr>
<table hight="10" colspan="2" bgcolor="#006699" align="center">
<font color="#EEEEEE" size="4">訪客留言</font>
</td>
</tr>
<tr>
<td height="30"  bgcolor="#99CCFF" align=""center">留言</td>
<td height="30" bgcolor="#99CCFF">
<input type="text" name="user" size="20" value="<?=$row['m_user']?>" disabled>
</td>
</tr>
<tr>
<td height="23"  bgcolor="#99CCFF" align=""center">留言</td>
<td height="23">
<input type="text" name="email" size="36" value="<?=$row['m_mail']?>"
</td>
</tr>
<tr>
<td height="23"  bgcolor="#99CCFF" align=""center">留言</td>
<td height="23" bgcolor="#99CCFF">
<input type="text" name="title" size="36" value="<?=$row['m_title']?>"
</td>
</tr>
<tr>
<td height="23"  bgcolor="#99CCFF" align=""center">留言</td>
<td height="80">
<p>
<textarea name="center" rows="10" cols="35"><?=$row['m_content']?></textarea>
<br>
</p>
</tr>
<tr>
<tr>
<td height="25" colspan="2" bgcolor="#006699">
<input type="reset" name="Reset" value="清除重填">
<input type="submit" name="Submit" value="送出留言">
</td>
</tr>
</table>
<input type="hidden" name="m_id" value="?<=$row['m_id']?>">
</td>
</tr>
</table>
</form>














































































