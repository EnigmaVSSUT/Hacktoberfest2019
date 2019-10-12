<?php
$events = array(
    'event1'=> array('image'=>'http://placehold.it/800x600/f44242/fff',  'title'=>'Event 1',  'text'=>'Lorem ipsum dolor sit amet consectetur adipisicing elit. Est, doloremque!',  'buttonText'=>'Go there',  'buttonLink'=>'#'),
    'event2'=> array('image'=>'http://placehold.it/800x600/f44242/fff',  'title'=>'Event 2',  'text'=>'Lorem ipsum dolor sit amet consectetur adipisicing elit. Est, doloremque!',  'buttonText'=>'Go there',  'buttonLink'=>'#'),
    'event3'=> array('image'=>'http://placehold.it/800x600/f44342/fff',  'title'=>'Event 2',  'text'=>'Lorem ipsum dolor sit amet consectetur adipisicing elit. Est, doloremque!',  'buttonText'=>'Go there',  'buttonLink'=>'#'),   
  );
class Events{
    public static function GenerateEvents($items){
        $html = "<div class='card-deck'>";
        foreach($items as $key => $item) {
          $html .= "<div class='card' style='width: 18rem;'>
          <img src='{$item['image']}' class='card-img-top' alt='...'>
          <div class='card-body'>
              <h5 class='card-title'>{$item['title']}</h5>
              <p class='card-text'>{$item['text']}</p>
              <a href='{$item['buttonLink']}' class='btn btn-primary'>{$item['buttonText']}</a>
          </div>
  </div>\n";
        }
        $html.="</div>";
        return $html;        
    }
}
?>
