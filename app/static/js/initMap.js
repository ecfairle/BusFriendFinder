function initMap() {
  var map = new google.maps.Map(document.getElementById('map'), {
    center: {lat: -34.397, lng: 150.644},
    zoom: 6
  });

  // Try HTML5 geolocation.
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(function(position) {
      var pos = {
        lat: position.coords.latitude,
        lng: position.coords.longitude
      };

      map.setCenter(pos);
      map.setZoom(16)

      var marker = new google.maps.Marker({
        draggable: true,
        position: pos, 
        map: map,
        title: "Your location"
      });

      google.maps.event.addListener(marker, 'dragend', function (event) {
          //alert(event.latLng.lat());
          //alert(event.latLng.lng());
      });

      google.maps.event.addListener(map, 'click', function(event) {
          marker.setPosition(event.latLng);
          //alert(event.latLng.lat());
          //alert(event.latLng.lng());
      });

    }, function() {
      handleLocationError(true, infoWindow, map.getCenter());
    });
  } else {
    // Browser doesn't support Geolocation
    handleLocationError(false, infoWindow, map.getCenter());
  }
}


function handleLocationError(browserHasGeolocation, infoWindow, pos) {
  infoWindow.setPosition(pos);
  infoWindow.setContent(browserHasGeolocation ?
                        'Error: The Geolocation service failed.' :
                        'Error: Your browser doesn\'t support geolocation.');
}