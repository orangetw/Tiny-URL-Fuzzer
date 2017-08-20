#!/usr/bin/php
<?php
    set_error_handler("warning_handler", E_WARNING|E_NOTICE);
    function warning_handler($errno, $errstr){
        exit(-1);
    }

    $url = $argv[1];
    echo file_get_contents($url);