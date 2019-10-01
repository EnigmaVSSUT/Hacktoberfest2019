<div class="container-fluid">
    <div class="row">
        <div class="col">
            <div class='jumbotron jumbotron-fluid mb-0'>
                <div class='container'>
                    <div class='row justify-content-center text-center'>
                        <div class='col-md-10 col-lg-6'>
                            <h1 style="font-family: 'Times New Roman', Times, serif;font-style: italic;">
                                <a href="" class="typewrite" data-period="2000"
                                    data-type='[ "Hi, Im Si.", "I am Creative.", "I Love Design.", "I Love to Develop." ]'>
                                    <span class="wrap"></span>
                                </a>
                            </h1>
                            <p class="lead"></p>
                            <p class='lead'>
                                <a class='btn btn-primary btn-lg' href='#' role='button'>Sponsor Us</a>
                            </p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <div class="row">
        <div class="row justify-content-center text-center">
            <div class='col-md-10 col-lg-8'>
                <?php require_once("./functions/SVG.php");?>
                <?php echo Paragraph::GenerateParagraph("Mechismu Racing is a student organization at IIT (ISM) Dhanbad, founded in 2008 with a vision to pioneer development and deployment of innovative technologies in the Indian Automobile Sector. We design, engineer and race our vehicles at SAE Collegiate Design Competitions like the Formula SAE and Baja SAE. Innovation and experimentation are the key drivers in our quest for excellence. Our achievements over the past three years stand testament to our engineering prowess. The team has always operated independently, transferring the knowledge obtained from year to year.","Why Sponsor Us?");?>
            </div>
        </div>
    </div>
</div>
<div class="row mb-2">
    <div class="container">
        <?php echo Sponsors::GenerateSponsors($Sponsors); ?>
    </div>
</div>
</div>