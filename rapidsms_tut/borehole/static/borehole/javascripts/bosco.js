var northCenter = new google.maps.LatLng(3.20487, 32.54885);

function initialize() {
	zoomCenter = northCenter;
	mapOptions = {
		center: northCenter,
		zoom: 9,
		mapTypeId: google.maps.MapTypeId.SATELLITE
	};
	
	map = new google.maps.Map(document.getElementById("map_canvas"), mapOptions);
	var regionKML = new google.maps.KmlLayer('http://www.lcmt.org/bosco/region_kml.php?f=4', {preserveViewport:true, clickable:false});
	regionKML.setMap(map);
	
	load_boreholes();
}
