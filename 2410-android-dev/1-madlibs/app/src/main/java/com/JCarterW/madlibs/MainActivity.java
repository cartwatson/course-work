package com.JCarterW.madlibs;

import androidx.appcompat.app.AppCompatActivity;
import androidx.appcompat.widget.AppCompatButton;
import androidx.appcompat.widget.AppCompatEditText;
import androidx.appcompat.widget.AppCompatTextView;

import android.annotation.SuppressLint;
import android.graphics.Color;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.LinearLayout;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        LinearLayout layout = new LinearLayout(this);
        // Name view
        AppCompatTextView nameView = new AppCompatTextView(this);
        nameView.setText("Name");

        //Edit Name
        final AppCompatEditText editName = new AppCompatEditText(this);
        final LinearLayout.LayoutParams params = new LinearLayout.LayoutParams(LinearLayout.LayoutParams.MATCH_PARENT, LinearLayout.LayoutParams.WRAP_CONTENT);
        editName.setLayoutParams(params);

        // Adjective view
        AppCompatTextView adjectiveView = new AppCompatTextView(this);
        adjectiveView.setText("Adjective");

        //Edit Adjective
        final AppCompatEditText editAdjective = new AppCompatEditText(this);
        final LinearLayout.LayoutParams params2 = new LinearLayout.LayoutParams(LinearLayout.LayoutParams.MATCH_PARENT, LinearLayout.LayoutParams.WRAP_CONTENT);
        editAdjective.setLayoutParams(params2);

        // Occupation view
        AppCompatTextView occupationView = new AppCompatTextView(this);
        occupationView.setText("Occupation");

        //Edit Occupation
        final AppCompatEditText editOccupation = new AppCompatEditText(this);
        final LinearLayout.LayoutParams params3 = new LinearLayout.LayoutParams(LinearLayout.LayoutParams.MATCH_PARENT, LinearLayout.LayoutParams.WRAP_CONTENT);
        editOccupation.setLayoutParams(params3);

        // Place view
        AppCompatTextView placeView = new AppCompatTextView(this);
        placeView.setText("Place");

        //Edit Place
        final AppCompatEditText editPlace = new AppCompatEditText(this);
        final LinearLayout.LayoutParams params4 = new LinearLayout.LayoutParams(LinearLayout.LayoutParams.MATCH_PARENT, LinearLayout.LayoutParams.WRAP_CONTENT);
        editPlace.setLayoutParams(params4);

        // Thing view
        AppCompatTextView thingView = new AppCompatTextView(this);
        thingView.setText("Thing");

        //Edit Thing
        final AppCompatEditText editThing = new AppCompatEditText(this);
        final LinearLayout.LayoutParams params5 = new LinearLayout.LayoutParams(LinearLayout.LayoutParams.MATCH_PARENT, LinearLayout.LayoutParams.WRAP_CONTENT);
        editThing.setLayoutParams(params5);

        // Name2 view
        AppCompatTextView name2View = new AppCompatTextView(this);
        name2View.setText("Name");

        //Edit Name2
        final AppCompatEditText editName2 = new AppCompatEditText(this);
        final LinearLayout.LayoutParams params6 = new LinearLayout.LayoutParams(LinearLayout.LayoutParams.MATCH_PARENT, LinearLayout.LayoutParams.WRAP_CONTENT);
        editName2.setLayoutParams(params6);

        //Message View
        final AppCompatTextView messageView = new AppCompatTextView(MainActivity.this);

        //button
        AppCompatButton button = new AppCompatButton(this);
        button.setText("Generate MadLib");
        final LinearLayout.LayoutParams params7 = new LinearLayout.LayoutParams(LinearLayout.LayoutParams.MATCH_PARENT, LinearLayout.LayoutParams.WRAP_CONTENT);
        button.setLayoutParams(params7);
        button.setOnClickListener(new View.OnClickListener() {
            @SuppressLint("SetTextI18n")
            @Override
            public void onClick(View view) {
                String name = editName.getText().toString();
                String adjective = editAdjective.getText().toString();
                String occupation = editOccupation.getText().toString();
                String place = editPlace.getText().toString();
                String thing = editThing.getText().toString();
                String name2 = editName2.getText().toString();

                messageView.setText(name + " is so " + adjective +". They are a "
                        + occupation + " They are always carries around a "
                        + thing + " and is contstantly chatting to "
                        + name2 + ". The icing on the cake though is that they spend so much money at "
                        + place + ". What a peculiar fellow.");
            }
        });

        layout.addView(nameView);
        layout.addView(editName);
        layout.addView(adjectiveView);
        layout.addView(editAdjective);
        layout.addView(occupationView);
        layout.addView(editOccupation);
        layout.addView(placeView);
        layout.addView(editPlace);
        layout.addView(thingView);
        layout.addView(editThing);
        layout.addView(name2View);
        layout.addView(editName2);
        layout.addView(button);
        layout.addView(messageView);
        layout.setOrientation(LinearLayout.VERTICAL);

        setContentView(layout);
    }
}
