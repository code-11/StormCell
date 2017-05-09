using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Unit : MonoBehaviour {

	public Sprite haloSprite;
	GameObject selectionHaloObj;

	public void onSelected(){
		//Only allow to be selected once
		if (transform.childCount == 0) {
			selectionHaloObj = new GameObject (); 
			//Center on parent
			selectionHaloObj.name = "Selection Halo";
			selectionHaloObj.transform.SetParent (gameObject.transform);
			selectionHaloObj.transform.localPosition = new Vector3 (0, 0, 0);
			selectionHaloObj.transform.localScale = new Vector3 (1, 1, 1);
			selectionHaloObj.AddComponent<SpriteRenderer> ();
			SpriteRenderer haloRenderer = selectionHaloObj.GetComponent<SpriteRenderer> ();
			haloRenderer.sprite = haloSprite;
			haloRenderer.color = Color.green;
			haloRenderer.sortingOrder=1;
		} else {
			Debug.Log (gameObject.name + " already has a halo");
			Debug.Log (gameObject.transform.GetChild (0).name);
		}
	
	}
}
