<?php
class TextBlock {
    public static function GenerateTextBlock($heading , $paragraph, $buttonLink, $buttonText) {
      $html="<div class='jumbotron jumbotron-fluid mb-0' id='mainJumbotron'>
      <div class='container'>
          <div class='row justify-content-center text-center'>
              <div class='col-md-10 col-lg-6'>
                  <h1 class='display-5'>{$heading}</h1>
                  <p class='lead'>{$paragraph}</p>
                  <p class='lead'>
                      <a class='btn btn-primary btn-lg' href='{$buttonLink}'role='button'>{$buttonText}</a>
                  </p>
              </div>
          </div>
      </div>
  </div>";
      return $html;
    }
  };
?>