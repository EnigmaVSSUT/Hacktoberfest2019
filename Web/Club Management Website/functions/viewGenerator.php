<?php
if(isset($_GET['url'])){
    $page = $_GET['url'];
    if(file_exists("views/".$page.".php")){
        require_once("views/".$page.".php");
        $title = "Mechismu | " . $page;
    }
    else{
        require_once("views/404.php");
        $title = "Oops! Looks Like You Are Lost";
    }
}
else{
    $page = "home";
    require_once("views/home.php");
    $title = "Mechismu | IIT ISM DHANBAD";
}
?>
<title><?php echo $title ;?></title>