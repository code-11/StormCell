﻿using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Unit : MonoBehaviour {

	public Sprite haloSprite;
	public GameObject selectionHaloObj;
	Vector3 goal;
	public int maxActionPoints=100;
	private int actionPoints;
	private bool moving=false;
	private bool selected=false;

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

	public void resetActionPoints(){
		actionPoints=maxActionPoints;
	}

	public void onSelected(){
		selected=true;
		//Only allow to be selected once
		if (selectionHaloObj == null) {
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
		}
	}

	public void onDeselected(){
		selected=false;
		Destroy(selectionHaloObj);
		selectionHaloObj=null;
	}

	public void setGoal(Vector3 loc){
		goal=loc;
	}

	public void moveToGoal(){
        transform.position = Vector3.MoveTowards(transform.position, goal, Time.deltaTime);
        moving = (goal!=transform.position);
	}

	public bool isMoving(){
		return moving;
	}
}
