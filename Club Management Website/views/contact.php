<link href='custom.css' rel='stylesheet' type='text/css'>
<div class="container">
    <div class="row">
        <!DOCTYPE html>
        <html>

        <head>
            <style>
            #map {
                height: 400px;
                width: 100%;
            }
            </style>
        </head>

        <body>
            <h3>Locate Us</h3>
            <div id="map"></div>
            <script>
            function initMap() {
                var uluru = {
                    lat: 28.501859,
                    lng: 77.410320
                };
                var map = new google.maps.Map(document.getElementById('map'), {
                    zoom: 4,
                    center: uluru
                });
                var marker = new google.maps.Marker({
                    position: uluru,
                    map: map
                });
            }
            </script>
            <script async defer src="https://maps.googleapis.com/maps/api/js?key= 
            AIzaSyBZ9e1cO3Mu1P9odTxZEORWaGW8ryhs6-E&callback=initMap">
            </script>
        </body>

        </html>
    </div>

    <div class="row">
        <div class="col-lg-8 col-lg-offset-2 py-5">
            <form id="contact-form" method="post" action="./views/ContactFunctions.php" role="form">
                <div class="messages"></div>

                <div class="controls">

                    <div class="row">
                        <div class="col-md-6">
                            <div class="form-group">
                                <label for="form_name">Firstname *</label>
                                <input id="form_name" type="text" name="name" class="form-control"
                                    placeholder="Please enter your firstname *" required="required"
                                    data-error="Firstname is required.">
                                <div class="help-block with-errors"></div>
                            </div>
                        </div>
                        <div class="col-md-6">
                            <div class="form-group">
                                <label for="form_lastname">Lastname *</label>
                                <input id="form_lastname" type="text" name="surname" class="form-control"
                                    placeholder="Please enter your lastname *" required="required"
                                    data-error="Lastname is required.">
                                <div class="help-block with-errors"></div>
                            </div>
                        </div>
                    </div>
                    <div class="row">
                        <div class="col-md-6">
                            <div class="form-group">
                                <label for="form_email">Email *</label>
                                <input id="form_email" type="email" name="email" class="form-control"
                                    placeholder="Please enter your email *" required="required"
                                    data-error="Valid email is required.">
                                <div class="help-block with-errors"></div>
                            </div>
                        </div>
                        <div class="col-md-6">
                            <div class="form-group">
                                <label for="form_phone">Phone</label>
                                <input id="form_phone" type="tel" name="phone" class="form-control"
                                    placeholder="Please enter your phone">
                                <div class="help-block with-errors"></div>
                            </div>
                        </div>
                    </div>
                    <div class="row">
                        <div class="col-md-12">
                            <div class="form-group">
                                <label for="form_message">Message *</label>
                                <textarea id="form_message" name="message" class="form-control"
                                    placeholder="Message for me *" rows="4" required="required"
                                    data-error="Please, leave us a message."></textarea>
                                <div class="help-block with-errors"></div>
                            </div>
                        </div>
                        <div class="col-md-12">
                            <input type="submit" class="btn btn-success btn-send" value="Send message">
                        </div>
                    </div>
                    <div class="row">
                        <div class="col-md-12">
                            <p class="text-muted"><strong>*</strong> These fields are required.
                        </div>
                    </div>
                </div>

            </form>

        </div><!-- /.8 -->

    </div> <!-- /.row-->

</div> <!-- /.container-->