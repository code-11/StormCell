import React, { Component } from "react";
import { connect } from 'react-redux'
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
// import countryData from "./countries";
import continentData from "./continents";
import Select from 'ol/interaction/Select';
import MapColorer from "./MapColorer";
import {getTime, pauseTime, startTime, getCountryShapes} from '../actions/index';
import { bindActionCreators } from 'redux';
import TimeControls from "./TimeControls";
//4326 - LAT LON
//3857 - X, Y

function mapStateToProps(state) {
  return {}
  // return { time: state.time };
}

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


// @connect((state) => {
//   return {
//     time: state.time
//   };
// })
class App extends Component {
  constructor(props) {
    super(props);

    this.state = {
      center: [0, 0],
      zoom: 1,
      selected: [],
    };

    this.countrySource = new VectorSource({
      format: new GeoJSON({dataProjection: 'EPSG:4326'})
    });

    const mapStyle = new Style({
          stroke: new Stroke({
              color: 'white',
              width: 1
          }),
          text: new Text(),
          fill: new Fill({
              color:"black",
          }),
      });

    const countryLayer= new VectorLayer({
      source: this.countrySource,
      style: (feature, res)=>{
          const text = mapStyle.getText();
          const name = feature.get('name');
          text.text_ = name;
          const fill = mapStyle.getFill();
          // console.log(fill);
          fill.setColor(this.mapColorer.determineColor(name));

          const stroke = mapStyle.getStroke();
          stroke.setColor(this.mapColorer.determineStroke(name));

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


    this.olmap.on('contextmenu', (evt) => {
      evt.preventDefault();
      console.log(this.state.selected);
    });

    this.olmap.on('click', (event)=> {
      const selectedCountry=this.olmap.forEachFeatureAtPixel(event.pixel, function(feature,layer) { return feature; });
      if (selectedCountry!==undefined){
        this.props.dispatch(getTime()).then(time=>{
          const selectedList=this.state.selected;
          const newSelectedVal=selectedCountry.values_.name;
          selectedList[0]=newSelectedVal
          this.setState({selected:selectedList});
          selectedCountry.changed();
        });
      }
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

    this.props.dispatch(getCountryShapes()).then(shapes=>{
      // this.setState({shapes: shapes});
      const countryShapes = this.props.store.getState().countryShapes;
      this.mapColorer = new MapColorer(countryShapes,continentData, this.state.selected);
      this.countrySource.addFeatures((new GeoJSON()).readFeatures(countryShapes));
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
      <div>
        <TimeControls store={this.props.store}/>
        <div id="map" style={{ width: "100%", height: "100vh" }}></div>
      </div>
    );
  }
}
export default connect(mapStateToProps)(App);
// export default connect(state => ({time: state.time}))(App);
// export default App;
