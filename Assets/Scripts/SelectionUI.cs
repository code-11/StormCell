﻿using UnityEngine;
using System.Collections;
using System.Collections.Generic;


/*Responsible for drawing the selection box, or other type of visual indication of selection.
 * The stores the units it found in selectedUnits where SelectionDisplay looks over it and does stuff*/
public class SelectionUI : MonoBehaviour {

	bool isSelecting = false;
	Vector3 mousePosition1;
	public List<Unit> selectedUnits = new List<Unit> ();
	GameObject ghost=null;
	// public SelectionDisplay selectionDisplay;
	static Texture2D _whiteTexture;
	public static Texture2D WhiteTexture
	{
		get
		{
			if( _whiteTexture == null )
			{
				_whiteTexture = new Texture2D( 1, 1 );
				_whiteTexture.SetPixel( 0, 0, Color.white );
				_whiteTexture.Apply();
			}

			return _whiteTexture;
		}
	}

	public static void DrawScreenRect( Rect rect, Color color )
	{
		GUI.color = color;
		GUI.DrawTexture( rect, WhiteTexture );
		GUI.color = Color.white;
	}
		
	public static void DrawScreenRectBorder( Rect rect, float thickness, Color color )
	{
		// Top
		DrawScreenRect( new Rect( rect.xMin, rect.yMin, rect.width, thickness ), color );
		// Left
		DrawScreenRect( new Rect( rect.xMin, rect.yMin, thickness, rect.height ), color );
		// Right
		DrawScreenRect( new Rect( rect.xMax - thickness, rect.yMin, thickness, rect.height ), color);
		// Bottom
		DrawScreenRect( new Rect( rect.xMin, rect.yMax - thickness, rect.width, thickness ), color );
	}
		
	public static Rect GetScreenRect( Vector3 screenPosition1, Vector3 screenPosition2 )
	{
		// Move origin from bottom left to top left
		screenPosition1.y = Screen.height - screenPosition1.y;
		screenPosition2.y = Screen.height - screenPosition2.y;
		// Calculate corners
		var topLeft = Vector3.Min( screenPosition1, screenPosition2 );
		var bottomRight = Vector3.Max( screenPosition1, screenPosition2 );
		// Create Rect
		return Rect.MinMaxRect( topLeft.x, topLeft.y, bottomRight.x, bottomRight.y );
	}
		
	public static Bounds GetViewportBounds( Camera camera, Vector3 screenPosition1, Vector3 screenPosition2 )
	{
		var v1 = Camera.main.ScreenToViewportPoint( screenPosition1 );
		var v2 = Camera.main.ScreenToViewportPoint( screenPosition2 );
		var min = Vector3.Min( v1, v2 );
		var max = Vector3.Max( v1, v2 );
		min.z = camera.nearClipPlane;
		max.z = camera.farClipPlane;

		var bounds = new Bounds();
		bounds.SetMinMax( min, max );
		return bounds;
	}

	private void pointSelect(){
		if (Input.GetMouseButtonDown (1) && selectedUnits.Count > 0) {
			Vector3 mousePos=Camera.main.ScreenToWorldPoint(Input.mousePosition);
			mousePos.z=0;
			foreach (Unit unit in selectedUnits){
				unit.setGoal(mousePos);
			}
			selectedUnits.Clear();
		}
	}


	void Update()
	{
		// If we press the left mouse button, save mouse location and begin selection
		if(Input.GetMouseButtonDown(0))
		{
			isSelecting = true;
			mousePosition1 = Input.mousePosition;
		}
		// If we let go of the left mouse button, end selection
		if (Input.GetMouseButtonUp(0)) {
			isSelecting = false;
			setUnitsAsSelected ();
			//Do something here if a unit is selected
			//selectionDisplay.onSelectedUnits (selectedUnits);
		}
		if (selectedUnits.Count!=0){
			pointSelect();
			ghostShowMovement();
		}
	}

	private void ghostShowMovement(){
		if (selectedUnits.Count==1){
			Vector3 mousePosition = Input.mousePosition;
            mousePosition = Camera.main.ScreenToWorldPoint(mousePosition);
            if (ghost==null){
            	GameObject selectedUnit=selectedUnits[0].gameObject;
            	ghost=Object.Instantiate(selectedUnit,selectedUnit.transform.position, Quaternion.identity);
            	ghost.GetComponent<Unit>().destroySelf();
            	Color ghostColor=ghost.GetComponent<SpriteRenderer>().color;
            	ghostColor.a=.1f;
            	ghost.GetComponent<SpriteRenderer>().color=ghostColor;
            }
            ghost.transform.position = Vector2.Lerp(ghost.transform.position, mousePosition, 1);
		}
	}

	// private void setUnitsAsDeselected

	private void setUnitsAsSelected(){
		selectedUnits = new List<Unit> ();
		foreach (Unit curUnit in GameObject.FindObjectsOfType<Unit>()) {
			if (IsWithinSelectionBounds (curUnit.gameObject)) {
				selectedUnits.Add (curUnit);
				curUnit.onSelected();
			}
		}
	}	

	public bool IsWithinSelectionBounds( GameObject gameObject )
	{
		var camera = Camera.main;
		var viewportBounds =
			GetViewportBounds( camera, mousePosition1, Input.mousePosition );

		return viewportBounds.Contains(
			camera.WorldToViewportPoint( gameObject.transform.position ) );
	}

	void OnGUI()
	{
		if( isSelecting )
		{
			// Create a rect from both mouse positions
			var rect = GetScreenRect( mousePosition1, Input.mousePosition );
			DrawScreenRect( rect, new Color( 0.8f, 0.8f, 0.95f, 0.25f ) );
			DrawScreenRectBorder( rect, 2, new Color( 0.8f, 0.8f, 0.95f ) );
		}
	}
}
