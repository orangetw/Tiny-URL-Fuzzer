#!/usr/bin/php
<?php
    $url = $argv[1];

    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, $url);
    if (curl_exec($ch) == false){
        exit(-1);
    }
    curl_close($ch);