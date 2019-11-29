<?php
session_start();
if (isset($_SESSION['user_name'])){
	$user_name = $_SESSION['user_name'];
}

foreach ($_COOKIE as $key => $val) {
	$_SESSION[$key] = $val;
}

/* removed everything because of undergoing investigation, please check dev and staging */
