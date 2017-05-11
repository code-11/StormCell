using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Unit : MonoBehaviour {

	public Sprite haloSprite;
	GameObject selectionHaloObj;
	Vector3 goal;
	public int maxActionPoints=100;
	private int actionPoints;

	void Start(){
		goal=transform.position;
		actionPoints=maxActionPoints;
	}

	void Update(){
		moveToGoal();
	}

	public void removeActionPoints(int amount){
		int toSet=Mathf.Max(actionPoints-amount,0);
		actionPoints=toSet;
	}

	public void destroySelf(){
		removeHalo();
		//Destroy(this);
	}

	public void removeHalo(){
		if (selectionHaloObj==null){
			Debug.Log("Halo already null");
		}
		Debug.Log("Removing Halo("+selectionHaloObj.name+") from "+gameObject.name);
		UnityEngine.Object.Destroy(selectionHaloObj);
	}

	public void resetActionPoints(){
		actionPoints=maxActionPoints;
	}

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

	public void setGoal(Vector3 loc){
		goal=loc;
	}

	public void moveToGoal(){
        transform.position = Vector3.MoveTowards(transform.position, goal, Time.deltaTime);
	}
}
