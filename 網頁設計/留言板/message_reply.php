<?
include("db_conn.php");
include("db_func.php");
$SQLStr = "SELECT* FROM message WHERE m_id='$m_id'";
$res = db_query("$SQLStr");
$row = db_fetch_array($res);
?>

<form name="from1" method="post" action="messenage_process.php?check=add">
<table width="481" border="1" cellpedding="0" cellspacing="0" align="center">
<tr>
<td>
<table width="480" border="0" cellpedding="1" cellspacing="1" align="center" bordercolor="#000099">
<tr>
<td  height="10" colspan="2" bgcolor="#006699">
<font color="#EEEEEE" size="4">訪客留言版</font>
</td>
</tr>
<tr>
<td height="30" bgcolor="#99CCFF">
<div align="center">留言人</div>
</td>
<td height="30" bgcolor="#99CCFF">
<input type="text" name="user" size="20">
</td>
</tr>
<tr>
<td height="23">
<div align="center">e-mail</div>
</td>
<td height="23">
<input type="text" name="email" size="36">
</td>
</tr>
<tr>
<td height="23" bgcolor="#99CCFF">
<div align="center">留言主題</div>
</td>
<td height="23" bgcolor="#99CCFF">
<!--------- 取出留言標題並限制不修改 --------->

<?php
$s="Re: ".$row['m_title']. ;
?>

<input type="text" name="title" size="36" value=<?=$s?> disabled>
</td>
</tr>
<tr>
<td height="80">
<div align="center">留言內容</div>
</td>
<td height="80">
<p>
<textarea name="content" rows="10" cols="35">
</textarea>
<br>
</p>
</td>
</tr>
<tr>
<td height="25" colspan="2" bgcolor="000000">
<input type"reset" name="Reset" value="1111">
<input type="submit" name="Submit" value="1111">
</td>
</tr>
</table>
</td>
</tr>
</table>
</form>




































