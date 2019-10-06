<div class="container-fluid">
    <div class="row">

        <div class="col"> <?php echo TextBlock::GenerateTextBlock("The Coolest Co-Working Space in Prague","Where you choose to work has impact on your productivity and creativity. It
                      also says a lot about your business. We are the right office space.","","Reserve Your
                      Spot");?></div>
    </div>
    <div class="row">
    </div>
    <div class="row mt-2">
        <div class="container">
            <div class="row justify-content-center text-center">
                <div class='col-md-10 col-lg-8'>
                    <?php require_once("./functions/SVG.php");?>
                    <?php echo Paragraph::GenerateParagraph("A team of dedicated under graduate engineers who put in all their efforts and passion to achieve their one and only goal to make a performance car.","Our Cars");?>
                </div>
            </div>
            <?php echo Cars::GenerateCars($cars); ?>
        </div>
    </div>
</div>
</div>