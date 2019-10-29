export default class MapColorer{
	constructor(countryData,continentData, selectedRef){

		this.storedColors={
	    };

	    this.usedColors={
	      "northamerica":[],
	      "southamerica":[],
	      "europe":[],
	      "africa":[],
	      "asia":[],
	      "oceania":[],
	      "antarctica":[]
	    }

	    this.countryData=countryData;
	    this.continentData=continentData;
	    this.selectedRef=selectedRef;
	}

	rgbToList(colorStr){
	  const rgbFrag=colorStr.replace(")","");
	  const rgbFrag2=rgbFrag.split("(")[1];
	  const rgb=rgbFrag2.split(",").map(x => parseInt(x));
	  return rgb;
	}

	rgbToStr(rgb){
	  return "rgb("+rgb+")"; 
	}

	bend(rgb,n){
	  const bentList=rgb.map(x=>x+n);
	  return bentList;
	  // return rgbToStr(bentList);
	}

	validRgb(rgb){
	  return !(rgb.map(x=>x>255).length>0);
	}

	determineStroke(country){
		  if(country==="Antarctica"){
		  	return "gray";
		  }
		  // else if(this.selectedRef.length>0 && country===this.selectedRef[0]){
    //         return "rgb(255,0,0)";
    //       }
          else{
            return "white";
          }
	}

	determineColor(country){
		const colorStr=this.determineColorCore(country);
		if(this.selectedRef.length>0 && country===this.selectedRef[0]){
			return "rgb(150,150,150)";
		}else{
			return colorStr;
		}
		return colorStr;
	}

	determineColorCore(country){

		const COLORS={
		  "northamerica":"rgb(137,140,255)",
		  "southamerica":"rgb(255,137,181)",
		  "europe":"rgb(255,220,137)",
		  "africa":"rgb(144,212,247)",
		  "asia":"rgb(245,162,111)",
		  "oceania":"rgb(207,243,129)",
		  "antarctica":"rgb(177,195,209)"};

		const continents= Object.keys(this.continentData);
		for(let i=0; i<continents.length; i+=1){
		  const continent = continents[i];
		  if (this.storedColors[country]!==undefined){
		    return this.rgbToStr(this.storedColors[country]);
		  }
		  if (this.continentData[continent][country] !== undefined){
		    let colorToUse=this.rgbToList(COLORS[continent]);
		    let bending=2;
		    while(this.usedColors[continent].includes(this.rgbToStr(colorToUse)) && this.validRgb(colorToUse)){
		      colorToUse=this.bend(colorToUse,bending);
		    }
		    if(!this.validRgb(colorToUse)){
		      colorToUse=this.rgbToList(COLORS[continent]);
		      bending=-2;
		      while(this.usedColors[continent].includes(this.rgbToStr(colorToUse))){
		        colorToUse=this.bend(colorToUse,bending);
		      }
		    }
		    this.usedColors[continent].push(this.rgbToStr(colorToUse));
		    this.storedColors[country]=colorToUse;

		    return this.rgbToStr(colorToUse);
		  }
		}
		return "rgb(255,255,255)";
	}

}