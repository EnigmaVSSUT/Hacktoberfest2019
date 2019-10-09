<?php
$cars = array(
    'car1'=> array('image'=>'http://placehold.it/800x600/f44242/fff',  'title'=>'Car 1',  'text'=>'Lorem ipsum dolor sit amet consectetur adipisicing elit. Est, doloremque!',  'buttonLink'=>'#',  'buttonText'=>'Go there',  'year'=>'2015'),
    'car2'=> array('image'=>'http://placehold.it/800x600/f44242/fff',  'title'=>'Car 2',  'text'=>'Lorem ipsum dolor sit amet consectetur adipisicing elit. Est, doloremque!',  'buttonLink'=>'#',  'buttonText'=>'Go there',  'year'=>'2015'),
    'car3'=> array('image'=>'http://placehold.it/800x600/f44242/fff',  'title'=>'Car 3',  'text'=>'Lorem ipsum dolor sit amet consectetur adipisicing elit. Est, doloremque!',  'buttonLink'=>'#',  'buttonText'=>'Go there',  'year'=>'2015'),
    'car4'=> array('image'=>'http://placehold.it/800x600/f44242/fff',  'title'=>'Car 4',  'text'=>'Lorem ipsum dolor sit amet consectetur adipisicing elit. Est, doloremque!',  'buttonLink'=>'#',  'buttonText'=>'Go there',  'year'=>'2015'),
  );
class Cars{
    public static function GenerateCars($items){
        $html = "<div class='card-deck'>";
        foreach($items as $key => $item) {
          $html .= "<div class='card' style='width: 18rem;'>
          <img src='{$item['image']}' class='card-img-top' alt='...'>
          <div class='card-body'>
          <h5 class='card-title'>{$item['title']}</h5>
              <p class='card-text'>{$item['text']}</p>
              <a href='#' class='btn btn-success'>{$item['year']}</a>
              <a href='{$item['buttonLink']}' class='btn btn-primary'>{$item['buttonText']}</a>              
          </div>
  </div>\n";
        }
        $html.="</div>";
        return $html;        
    }
}
?>
