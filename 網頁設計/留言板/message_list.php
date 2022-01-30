<?php
$s="aaaa";
?>
<input type="text" name="title" size="36" value=<?=$s?> disabled>

<table width="750" align="center"  border="0" cellpadding="0" cellspacing="1">    
<tr bgcolor="#0066CC">
<td width="375" align="center">
<a href = " message_post.php "> 新增留言 </a>
</td>
<td width="375" align="center">
<a href = " message_list.php?p=0 "> 回首頁 </a>
</td>
</tr>
<tr bgcolor="#0066CC">
<td width="290" align="center">
<font color="#FFFFFF">留言主題</font>
</td>
<td width="300" align="center">
<font color="#FFFFFF">留言內容</font>
</td>
<td width="60" >
<font color="#FFFFFF">留言人</font>
</td>
<td width="100" >
<font color="#FFFFFF">留言時間</font>
</td>
</tr>

<?php
//================================初值設定======================================
include("db_conn.php"); //代入連線
include("db_func.php"); //代入功能
$SQLStr = "SELECT * FROM message ORDER BY m_time DESC";  //選擇message資料庫並依照元素m_time排序 由大到小
$res = db_query($SQLStr);       //傳入上述
$p=0; //初值代入
try                //嘗試
{ 
  $p=$_GET[p];     //資料當前頁面第一筆讀取
}
catch(Exception $e)
{
}
//==============================================================================
//================================資料寫入======================================
if(db_num_rows($res)>0) //資料筆數 大於 0
{
	$num = db_num_rows($res); //$num=資料筆數
	$check = $p+10;           //當前頁面最後一筆編號
	for ($i=0;$i<=$num;$i++)              
  {
	   $row= db_fetch_array($res); //陣列資訊儲存
	   if($i>=$p && $i<$check) //從$p開始後10筆
	   {                          
	      if($i%2 == 0) echo"<tr bgcolor = '#DDDDDD'>"; //雙色欄位製作 有色欄位 
		    else echo"<tr>";                              //雙色欄位製作 無色欄位
        //==
        if(strlen($row['m_title'])>15) // m_title中字串長度大於15 時
	      {
		      echo "<td width= '280'><a href='message_show.php?m_id=" .$row['m_id']."'>";
		      echo substr($row['m_title'],0,30) . "...</a></td>";                         //輸出陣列 m_title中字串(限制最大30字)  鏈接:show
	      }
	      else
	      {
		      echo "<td width= '280'><a href='message_show.php?m_id=" .$row['m_id']."'>";
		      echo $row['m_title'] . "</a></td>";                                         //輸出陣列 m_title中字串(無限制) 鏈接show
	      }
        //==
	      if(stristr($row['m_content'],"<br>"))//???陣列 m_content 有換行時                                         
	      {
	        echo "<td width='300'><a href='message_show.php?m_id=" .$row['m_id']."'>";
	        echo substr($row['m_content'],0,0  - strlen(strstr($row['m_content'],"<br>"))). "...</a></td>";     //???輸出陣列 m_content中字串換行後資訊 鏈接show
	      }
	      else
	      {
		      echo "<td width= '300'><a href='message_show.php?m_id=" .$row['m_id']."'>";                         //輸出陣列 m_content中字串(無限制) 鏈接show
		      echo $row['m_content'] . "</a></td>";
        }
        //==
	      echo "<td width= '60' align='center'><a href='mailto:".$row['m_mail']."'>" . $row['m_user']."</a></td>";    //輸出陣列 m_user中字串 鏈接:mailto:email
        echo "<td width= '130' align='center'>" .substr($row['m_time'],0,16)."</td>";                               //輸出陣列 m_time中字串(限制最大16字)
	      echo "</tr>";  //雙色欄位製作 結尾
	      $j = $i+1; //等同於$check 當前頁面最後一筆編號
	   }
  }
}
//==============================================================================
?>
</table>



<br>



<table width="406" align="center" border="0">
<tr>
<td align="center">
<a href='message_list.php?p='>第一頁</a>
</td>

<td align="center">
<?php
if($p>9)//資料位置大於9筆 時
{
    $last = (floor($j/10)*10)-10; //減10
    echo "<a href='message_list.php?p=" .$last. "'>上一頁</a>";  //???當前頁面最後一筆資料-10=當前第一筆資料 從新讀取
}
else echo "上一頁";
?>
</td>

<td align="center">
<?php
if($i>9 && $num>$check) //資料總筆數大於 9 和 總筆數大於 當前頁面最後一筆位置 時
echo "<a href='message_list.php?p=".$j."'>下一頁</a>";  //當前頁面最後一筆開始 從新讀取往後資訊
else
echo "下一頁";
?>
</td>

<td align"center">
<?php
if($i>9) //資料總筆數大於 9
{
$final= floor($num/10)*10; //資料總筆數去除個位數
echo "<a href='message_list.php?p=$final'>末一頁</a>"; //資料總筆數去除個位數開始 從新讀取往後資訊
}
else
	echo "末一頁";
?>
</td>


</table>








































