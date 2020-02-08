<?php
require 'vendor/autoload.php';

use \Firebase\JWT\JWT;

if(isset($_COOKIE["access"]))
{
	$key = '_S0_R@nd0m_P@ss_';
	$decoded = JWT::decode($_COOKIE["access"], base64_decode(strtr($key, '-_', '+/')), ['HS256']);
	if($decoded->access_code === "0E76658526655756207688271159624026011393")
	{
		header("Location: 7F2xxxxxxxxxxxxx/");
	}
	else
	{
		header("Location: index.html");
	}
}
else
{
	$token_payload = [
	  'project' => 'PlayBuff',
	  'access_code' => 'C0B137FE2D792459F26FF763CCE44574A5B5AB03'
	];
	$key = '_S0_R@nd0m_P@ss_';
	$jwt = JWT::encode($token_payload, base64_decode(strtr($key, '-_', '+/')), 'HS256');
	$cookiename = 'access';
	setcookie('access',$jwt, time() + (86400 * 30), "/");
	header("Location: index.html");
}

?>
