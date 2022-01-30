<?php
function db_query($qry_str){return mysql_query($qry_str);}
function db_num_rows($res){return mysql_num_rows($res);}
function db_fetch_object($res){return mysql_fetch_object($res);}
function db_fetch_array($res){return mysql_fetch_array($res);}
function db_data_seek($res,$num){return mysql_data_seek($res,$num);}
function db_instert_id($res){return mysql_insert_id($res);}
?>







































