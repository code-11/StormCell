import React from 'react';
import Title from './Title';
import AddTask from './AddTask';
import Board from './Board';
import './App.css';

import {
  interaction, layer, custom, control, //name spaces
  Interactions, Overlays, Controls,     //group
  Map, Layers, Overlay, Util    //objects
} from "react-openlayers";

const App = () => (
    // <div>
    //     <Title />
    //     <AddTask />
    //     <Board />
    // </div>
    <Map view={{center: [0, 0], zoom: 2}}>
      <Layers>
        <layer.Tile/>
      </Layers>
      <Controls attribution={false} zoom={true}>
        <control.Rotate />
        <control.ScaleLine />
        <control.FullScreen />
        <control.OverviewMap />
        <control.ZoomSlider />
        <control.ZoomToExtent />
        <control.Zoom />
      </Controls>
      <Interactions>
      </Interactions>
    </Map>
);

export default App;