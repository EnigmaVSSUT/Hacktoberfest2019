<?php

  /**
   * Get Website Content
   */
  function curl($url)
  {
    $ch = curl_init();
    
    curl_setopt($ch, CURLOPT_URL, $url);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
    curl_setopt($ch, CURLOPT_FOLLOWLOCATION, 1);
    curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, 0);
    
    $result_raw = curl_exec($ch);
    
    return $result_raw;
  }
