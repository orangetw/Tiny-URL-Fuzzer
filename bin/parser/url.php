#!/usr/bin/php
<?php
	error_reporting(0);
	$url = $argv[1];
	$x = parse_url($url);
	printf("scheme=%s, host=%s, port=%s", $x['scheme'], $x['host'], $x['port']);