import React from 'react';
import './App.css';

import {
  interaction, layer, custom, control, //name spaces
  Interactions, Overlays, Controls,     //group
  Map, Layers, Overlay, Util    //objects
} from "react-openlayers";

const App = () => (
    <Map view={{center: [0, 0], zoom: 2}}>
      <Layers>
        <layer.Tile/>
      </Layers>
      <Controls attribution={false} zoom={false}>
        <control.Rotate />
      </Controls>
      <Interactions>
      </Interactions>
    </Map>
);

export default App;