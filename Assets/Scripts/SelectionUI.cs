using UnityEngine;
using System.Collections;
using System.Collections.Generic;


/*Responsible for drawing the selection box, or other type of visual indication of selection.
 * The stores the units it found in selectedUnits where SelectionDisplay looks over it and does stuff*/
public class SelectionUI : MonoBehaviour {

	bool isSelecting = false;
	public Unit selectedUnit = null;
	GameObject ghost=null;
	LineRenderer lineRenderer=null;
	Material lineRendererMaterial=null;
	private float ghostAlpha=.2f;
	// public SelectionDisplay selectionDisplay;

	private void pointSelect(){
		if (Input.GetMouseButtonDown (1) && selectedUnit!=null) {
			Vector3 mousePos=Camera.main.ScreenToWorldPoint(Input.mousePosition);
			mousePos.z=0;
			if (!selectedUnit.isMoving()){
				selectedUnit.setGoal(mousePos);
			}
		}
	}


	void Update()
	{
		if(Input.GetMouseButtonDown(0))
		{
			isSelecting = true;
			setUnitAsDeselected();
			removeGhost();
			setUnitAsSelected ();
		}
		if (selectedUnit!=null){
			pointSelect();
			ghostShowMovement();
		}
	}

	private void removeGhost(){
		Destroy(ghost);
		Destroy(lineRenderer);
	}

	private void ghostShowMovement(){
		if (selectedUnit!=null){
			Vector3 mousePosition = Input.mousePosition;
            mousePosition = Camera.main.ScreenToWorldPoint(mousePosition);
            if (ghost==null){
            	ghost=Object.Instantiate(selectedUnit.gameObject,selectedUnit.transform.position, Quaternion.identity);
            	//Remove the selection halo
            	if (ghost.transform.childCount>0){
            		Destroy(ghost.transform.GetChild(0).gameObject);
            	}
            	Destroy(ghost.GetComponent<Unit>());
            	Color ghostColor=ghost.GetComponent<SpriteRenderer>().color;
            	ghostColor.a=ghostAlpha;
            	ghost.GetComponent<SpriteRenderer>().color=ghostColor;
            }
            if (lineRenderer==null){
            	lineRenderer= ghost.AddComponent<LineRenderer>();
            	lineRenderer.material = lineRendererMaterial;
            	Color selectionColor=Color.white;
            	selectionColor.a=ghostAlpha;
            	lineRenderer.material.color=selectionColor;
            	lineRenderer.startWidth=0.05F;
            	lineRenderer.endWidth=0.05F;
		 		lineRenderer.positionCount=2;
            }
            lineRenderer.SetPosition(0,selectedUnit.gameObject.transform.position);
            lineRenderer.SetPosition(1,mousePosition);
            ghost.transform.position = Vector2.Lerp(ghost.transform.position, mousePosition, 2);
		}
	}

	private void setUnitAsDeselected(){
		if (selectedUnit!=null){
			selectedUnit.onDeselected();
		}
	}

	private void setUnitAsSelected(){
		Collider2D hitInfo =Physics2D.OverlapPoint(Camera.main.ScreenToWorldPoint(Input.mousePosition));
		if (hitInfo!=null){
			selectedUnit=hitInfo.gameObject.GetComponent<Unit>();
			selectedUnit.onSelected();
		}else{
			selectedUnit=null;
			Debug.Log("Missed");
		}
	}
}
