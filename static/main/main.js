;(function($, L){
	
	// Map
	var map = L.map('map', {
		center: L.latLng(38.4992544,-96.0210078),
		zoom: 4,
	});
	
	// Layer
	L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(map);
	// var mapbox_access_token = 'pk.eyJ1IjoidWdpbnJvb3QiLCJhIjoiY2lzdG9odGo3MDAwNjJ4bGd2ZWg1M3YweiJ9.91Bb0nlFUijKrL-piO5tZQ';
	// L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=' + mapbox_access_token).addTo(map);
	


	// My geojson
	var geojson = L.geoJson($_PARAMS.geojson, {
		
		// Style
		style: function (feature) {
			var getColor = function (d) {
				var colors = [
					[1000, '#800026'],
					[500 , '#BD0026'],
					[200 , '#E31A1C'],
					[100 , '#FC4E2A'],
					[50  , '#FD8D3C'],
					[20  , '#FEB24C'],
					[10  , '#FED976'],
					[0   , '#FFEDA0'],
				];
				
				for(var i in colors){
					if(d > colors[i][0]){
						return colors[i][1]
					}
				}
				return colors[colors.length - 1][1];
			}
			return {
				fillColor: getColor(feature.properties.density),
				weight: 2,
				opacity: 1,
				color: 'white',
				dashArray: '3',
				fillOpacity: 0.7
			};
		},
		
		
		// Events
		onEachFeature: function onEachFeature(feature, layer) {
			layer.on({
				
				mouseover: function(e) {
					var layer = e.target;

					layer.setStyle({
						weight: 5,
						color: '#666',
						dashArray: '',
						fillOpacity: 0.7
					});

					if (!L.Browser.ie && !L.Browser.opera && !L.Browser.edge) {
						layer.bringToFront();
					}
					fPrintInfo(layer.feature.properties)
				},
				
				mouseout: function(e) {
					geojson.resetStyle(e.target);
					fPrintInfo();
				},
				
				click: function(e) {
					map.fitBounds(e.target.getBounds());
				}
			});
		}
	}).addTo(map);
	
	// Info, outher map
	var fPrintInfo = (function(data){
		var $state = $('.main-info-text-state');
		var $density = $('.main-info-text-density');
		var default_state = $state.html();
		var default_density = $density.html();
		return function(data){
			if(data){
				$state.html('<b>' + data.name + '</b>').addClass('main-info-text-select');
				$density.html(data.density + ' people / mi<sup>2</sup>').addClass('main-info-text-select');
			}else{
				$state.html(default_state).removeClass('main-info-text-select');
				$density.html(default_density).removeClass('main-info-text-select');
			}
		}
	}());
}(jQuery, L));











