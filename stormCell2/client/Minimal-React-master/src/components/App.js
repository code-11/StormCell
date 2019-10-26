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

//4326 - LAT LON
//3857 - X, Y

class App extends Component {
  constructor(props) {
    super(props);

    this.state = { center: [0, 0], zoom: 1 };

    const countryLoader = new VectorSource({
      format: new GeoJSON({dataProjection: 'EPSG:4326'})
    })
    countryLoader.addFeatures((new GeoJSON()).readFeatures(countryData));

    const style = new Style({
          stroke: new Stroke({
              color: 'black',
              width: 1
          }),
          text: new Text(),
      });

    const countryLayer= new VectorLayer({
      source: countryLoader,
      style: function(feature, res){
          const text = style.getText();
          text.text_ = feature.get('name');
          return style;
      }
    });

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