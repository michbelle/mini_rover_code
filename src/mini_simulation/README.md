## mini simulation code

build on jazzy


## bug TOFIX

this can be defined only one time, if there are 2 robots with this gazebo crash

for now is commented in mini, but not in jobot

it need to be added to the world


```xml
<gazebo>    
    <plugin filename="libignition-gazebo-sensors-system.so" name="ignition::gazebo::systems::Sensors">
        <render_engine>ogre2</render_engine>
    </plugin>
</gazebo>
```