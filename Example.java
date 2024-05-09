import java.io.*;
import java.awt.*;
import java.awt.event.*;
public class Example extends frame implements keyeventlistener
{
	label l;
	TextArea area;
     Example()
	{
		l=new Label();
		l.setBounds(20,50,100,20);
		area.setBounds(20,80,300,300);
		add(l);
		add(area);
		setSize(400,400);
		setLayout(null);
		setVisible(true);
		addkeyeventlistener();
	}
	public void keyPressed(keyEvent e)
	{
		l.setText("key pressed");
	}
	public void keyReleased(keyevent e)
	{
		l.setText("key Released");
	}
	public void keyTyped(keyevent e)
	{
		l.setText("key Typed");
	}
	public static void main(String args[])
	{
		new Example();
	}
}