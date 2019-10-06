<div class="container-fluid">
    <div class="row mb-3">
        <div class="col">
            <?php echo TextBlock::GenerateTextBlock("Mechismu | Racing","A team of dedicated under graduate engineers who put in all their efforts and passion to achieve their one and only goal to make a performance car.","#","Are You Excited!");?>
        </div>
    </div>
    <section id="sec-about" class="sec-about pt-5 pb-5">
        <div class="container">
            <div class="row justify-content-center text-center">
                <div class='col-md-10 col-lg-8'>
                    <?php require_once("./functions/SVG.php");?>
                    <?php echo Paragraph::GenerateParagraph("Mechismu Racing is a student organization at IIT (ISM) Dhanbad, founded in 2008 with a vision to pioneer development and deployment of innovative technologies in the Indian Automobile Sector. We design, engineer and race our vehicles at SAE Collegiate Design Competitions like the Formula SAE and Baja SAE. Innovation and experimentation are the key drivers in our quest for excellence. Our achievements over the past three years stand testament to our engineering prowess. The team has always operated independently, transferring the knowledge obtained from year to year. ","About Us");?>
                </div>
            </div>
            <div class="row mt-4">
                <div class="col-sm-4">
                    <h4>35</h4>

                    <hr />

                    <h5>
                        students</h5>
                </div>

                <div class="col-sm-4">
                    <h4>8</h4>

                    <hr />

                    <h5>departments</h5>
                </div>

                <div class="col-sm-4">
                    <h4>1</h4>

                    <hr />

                    <h5>car</h5>
                </div>
            </div>
            <div class="row mt-4">
                <div class="gallery-wrap">
                    <div class="item item-1"></div>
                    <div class="item item-2"></div>
                    <div class="item item-3"></div>
                    <div class="item item-4"></div>
                    <div class="item item-5"></div>
                </div>
            </div>
        </div>

</div>
</section>
<div class="row justify-content-center text-center">
        <div class='col-md-10 col-lg-8'>
            <?php require("./functions/SVG.php");?>
            <?php echo Paragraph::GenerateParagraph("Mechismu Racing is a student organization at IIT (ISM) Dhanbad, founded in 2008 with a vision to pioneer development and deployment of innovative technologies in the Indian Automobile Sector. We design, engineer and race our vehicles at SAE Collegiate Design Competitions like the Formula SAE and Baja SAE. Innovation and experimentation are the key drivers in our quest for excellence. Our achievements over the past three years stand testament to our engineering prowess. The team has always operated independently, transferring the knowledge obtained from year to year. ","Our Achievements");?>
        </div>
    </div>
    <div class="container">
    <?php echo Achievements::GenerateAchievements($achievements); ?>
    </div>

</div>
</div>