<?php
$teams = array(
    'Member1'=> array('image'=>'http://placehold.it/800x600/f44242/fff',  'name'=>'Member 1',  'text'=>'Lorem ipsum dolor sit amet consectetur adipisicing elit. Est, doloremque!',  'instagramLink'=>'#',  'twitterLink'=>'#',  'facebookLink'=>'#',  'linkedinLink'=>'#'),
    'Member2'=> array('image'=>'http://placehold.it/800x600/f44242/fff',  'name'=>'Member 2',  'text'=>'Lorem ipsum dolor sit amet consectetur adipisicing elit. Est, doloremque!',  'instagramLink'=>'#',  'twitterLink'=>'#',  'facebookLink'=>'#',  'linkedinLink'=>'#'),
    'Member3'=> array('image'=>'http://placehold.it/800x600/f44342/fff',  'name'=>'Member 2',  'text'=>'Lorem ipsum dolor sit amet consectetur adipisicing elit. Est, doloremque!',  'instagramLink'=>'#',  'twitterLink'=>'#',  'facebookLink'=>'#',  'linkedinLink'=>'#'),
    'Member3'=> array('image'=>'http://placehold.it/800x600/f44342/fff',  'name'=>'Member 2',  'text'=>'Lorem ipsum dolor sit amet consectetur adipisicing elit. Est, doloremque!',  'instagramLink'=>'#',  'twitterLink'=>'#',  'facebookLink'=>'#',  'linkedinLink'=>'#'),
    'Member3'=> array('image'=>'http://placehold.it/800x600/f44342/fff',  'name'=>'Member 2',  'text'=>'Lorem ipsum dolor sit amet consectetur adipisicing elit. Est, doloremque!',  'instagramLink'=>'#',  'twitterLink'=>'#',  'facebookLink'=>'#',  'linkedinLink'=>'#'),
    'Member3'=> array('image'=>'http://placehold.it/800x600/f44342/fff',  'name'=>'Member 2',  'text'=>'Lorem ipsum dolor sit amet consectetur adipisicing elit. Est, doloremque!',  'instagramLink'=>'#',  'twitterLink'=>'#',  'facebookLink'=>'#',  'linkedinLink'=>'#'),   
  );
class Team{
    public static function GenerateTeam($items){
        $html = "<div class='card-deck'>";
        foreach($items as $key => $item) {
          $html .= "<div class='card' style='width: 18rem;'>
          <img src='{$item['image']}' class='card-img-top' alt='...'>
          <div class='card-body'>
              <h5 class='card-title'>{$item['name']}</h5>
              <p class='card-text'>{$item['text']}</p>
              <a href='{$item['instagramLink']}'><i class='fa fa-instagram'></i></a>
              <a href='{$item['twitterLink']}'><i class='fa fa-twitter'></i></a>
              <a href='{$item['linkedinLink']}'><i class='fa fa-linkedin'></i></a>
              <a href='{$item['facebookLink']}'><i class='fa fa-facebook'></i></a>
          </div>
        </div>\n";
        }
        $html.="</div>";
        return $html;        
    }
}
?>
