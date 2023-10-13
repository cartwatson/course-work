package com.usu.rougelikev2.game.gameobjects

import android.graphics.Canvas
import android.graphics.Color
import android.graphics.Paint
import com.usu.rougelikev2.game.gameengine.Game
import com.usu.rougelikev2.game.gameengine.GameObject
import com.usu.rougelikev2.game.gameengine.Location


class Key(game: Game?) : GameObject(game!!) {
    override fun render(canvas: Canvas, paint: Paint) {
//        things you can do in this render method for reference.
//        val coords: Location = state["coords"] // gets the location of the object in the grid
//        val cellSize: Int = game.gameState["cellSize"] // gets the size of each cell in the game
//        val myX = coords.x * cellSize // gets the current x position (in pixels) in screen space
//        val myY = coords.y * cellSize // gets the current y position (in pixels) in screen space
//        val isActive: Boolean = state.get("active") // get whether the key is active or not (not active means the player already picked it up)
        val isActive: Boolean = state["active"]
        if (!isActive) return
        val coords: Location = state["coords"]
        val cellSize: Int = game.gameState["cellSize"]
        val myX = coords.x * cellSize
        val myY = coords.y * cellSize
        canvas.translate(myX, myY)
        val size = cellSize.toFloat()

        // top circle
        paint.color = Color.rgb(80,80,80)
        canvas.drawOval(20f, 20f, size-20f, size/2, paint)
        canvas.drawRect(size/2-15f, size/2-20f, size/2+15f, size-20f, paint)
        paint.color = Color.rgb(255,215,0)
        canvas.drawOval(20f+2f, 20f+2f, size-20f-2f, size/2-2f, paint)
        canvas.drawRect(size/2-15f+2f, size/2-20f+2f, size/2+15f-2f, size-20f-2f, paint)
        // key hole at the top

        // key/pins
        paint.color = Color.rgb(80,80,80)
        canvas.drawRect(size/2, size/2+5f, size/2+30f, size/2+20f, paint)
        canvas.drawRect(size/2, size/2+30f, size/2+30f, size/2+45f, paint)
        paint.color = Color.rgb(255,215,0)
        canvas.drawRect(size/2, size/2+5f+2f, size/2+30f-2f, size/2+20f-2f, paint)
        canvas.drawRect(size/2, size/2+30f+2f, size/2+30f-2f, size/2+45f-2f, paint)
    }

    init {
        state["active"] = true
    }
}