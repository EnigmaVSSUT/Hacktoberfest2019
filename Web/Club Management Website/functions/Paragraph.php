<?php
class Paragraph{
    public static function GenerateParagraph($paragraph,$heading) {
      $html="<h1 class='h4'>{$heading}</h1>
      <p class='mt-4 mb-4'>{$paragraph}</p>";
      return $html;
    }
  };
?>
