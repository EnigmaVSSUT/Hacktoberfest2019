<?php
$menu = array(
    'home'   => array('text'=>'Home',  'url'=>'?url=home',  'icon'=>'fa fa-home'),
    'about'  => array('text'=>'About FSAE',  'url'=>'?url=about',  'icon'=>'fa fa-flag'),
    'cars'   => array('text'=>'Cars', 'url'=>'?url=cars',  'icon'=>'fa fa-car'),
    'team'   => array('text'=>'Team', 'url'=>'?url=team',  'icon'=>'fa fa-users'),
    'sponsors' => array('text'=>'Sponsors', 'url'=>'?url=sponsors',  'icon'=>'fa fa-money'),
    'contact' => array('text'=>'Contact Us', 'url'=>'?url=contact',  'icon'=>'fa fa-id-card'),
  );
  class Navigation {
    public static function GenerateMenu($items) {
      $html = '<ul class="navbar-nav">';
      foreach($items as $key => $item) {
        $selected = (isset($_GET['url'])) && $_GET['url'] == $key ? 'active' : null;
        $html .= "<li class='nav-item {$selected}'>
        <a class='nav-link' href='{$item['url']}'>
        <i class='{$item['icon']}'></i>
        {$item['text']}
        </a>
        </li>\n";
      }
      $html .= "  </ul>\n";
      return $html;
    }
  };
?>