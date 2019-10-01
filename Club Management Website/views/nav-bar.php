<nav class="navbar navbar-icon-top navbar-expand-lg navbar-dark bg-dark sticky-top">
<button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <a class="navbar-brand" href="#">
    <img src="https://getBootStrap.com/docs/4.3/assets/brand/bootstrap-solid.svg" width="30" height="30" alt="">
  </a>
  <div class="collapse navbar-collapse flex-row-reverse" id="navbarSupportedContent">
    <?php echo Navigation::GenerateMenu($menu); ?>
  </div>
</nav>