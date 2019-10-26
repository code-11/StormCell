import React, { Component } from "react";
import 'ol/ol.css';
import GeoJSON from 'ol/format/GeoJSON';
import Map from 'ol/Map';
import VectorLayer from 'ol/layer/Vector';
import VectorSource from 'ol/source/Vector';
import TileLayer from 'ol/layer/Tile';
import OSM from 'ol/source/OSM';
import View from 'ol/View';
import Style from 'ol/style/Style';
import Text from 'ol/style/Text';
import Stroke from 'ol/style/Stroke';
import Fill from 'ol/style/Fill';
import countryData from "./countries";
import Select from 'ol/interaction/Select';
//4326 - LAT LON
//3857 - X, Y

function hash(str) {
  var hash = 5381,
      i    = str.length;

  while(i) {
    hash = (hash * 33) ^ str.charCodeAt(--i);
  }

  /* JavaScript does bitwise operations (like XOR, above) on 32-bit signed
   * integers. Since we want the results to be always positive, convert the
   * signed int to an unsigned by doing an unsigned bitshift. */
  return hash >>> 0;
}

function hashTo(str,n){
  return hash(str) % n;
}

class App extends Component {
  constructor(props) {
    super(props);

    const COLORS=[
      "rgb(137,140,255)",
      "rgb(255,137,181)",
      "rgb(255,220,137)",
      "rgb(144,212,247)",
      "rgb(245,162,111)",
      "rgb(207,243,129)",
      "rgb(177,195,209)"];

    this.state = { center: [0, 0], zoom: 1 };

    const countryLoader = new VectorSource({
      format: new GeoJSON({dataProjection: 'EPSG:4326'})
    })
    countryLoader.addFeatures((new GeoJSON()).readFeatures(countryData));

    const mapStyle = new Style({
          stroke: new Stroke({
              color: 'black',
              width: 1
          }),
          text: new Text(),
          fill: new Fill({
              color:"white",
          }),
      });

    const countryLayer= new VectorLayer({
      source: countryLoader,
      style: function(feature, res){
          const text = mapStyle.getText();
          text.text_ = feature.get('name');
          const fill = mapStyle.getFill();
          // console.log(fill);
          fill.setColor(COLORS[hashTo(feature.get("name"),COLORS.length)]);
          return mapStyle;
      }
    });

    const selectClick = new Select();

    this.olmap = new Map({
      target: 'map-container',
      layers:[
        countryLayer,
      ],
      view: new View({
        center: [0, 0],
        zoom: 2,
        projection: 'EPSG:4326'
      })
    });

    this.olmap.on('click', (event)=> {
      const selected=this.olmap.forEachFeatureAtPixel(event.pixel, function(feature,layer) { return feature; });
      console.log(selected);
    });
  }

  updateMap() {
    this.olmap.getView().setCenter(this.state.center);
    this.olmap.getView().setZoom(this.state.zoom);
  }

  componentDidMount() {
    this.olmap.setTarget("map");

    // Listen to map changes
    this.olmap.on("moveend", () => {
      let center = this.olmap.getView().getCenter();
      let zoom = this.olmap.getView().getZoom();
      this.setState({ center, zoom });
    });
  }

  shouldComponentUpdate(nextProps, nextState) {
    let center = this.olmap.getView().getCenter();
    let zoom = this.olmap.getView().getZoom();
    if (center === nextState.center && zoom === nextState.zoom) return false;
    return true;
  }

  userAction() {
    this.setState({ center: [546000, 6868000], zoom: 5 });
  }

  render() {
    this.updateMap(); // Update map on render?
    return (
      <div id="map" style={{ width: "100%", height: "100vh" }}>
      </div>
    );
  }
}

export default App;