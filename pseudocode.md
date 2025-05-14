# FIRST PSEUDOCODE
// --- Initialization ---
Initialize EV3 sensors (color sensor, ultrasonic sensor, motor ports)
Define target color RED
Define target color YELLOW
Define red_dropoff_position  // Coordinates or relative location
Define yellow_dropoff_position // Coordinates or relative location
Define search_speed
Define transport_speed
Define obstacle_avoidance_distance

// --- Main Program ---

// --- Collect Red Block ---
Function collect_red_block():
  While red_block_found is FALSE:
    Move forward at search_speed
    If ultrasonic sensor detects obstacle within obstacle_avoidance_distance:
      Perform obstacle_avoidance()
    If color sensor detects target color RED:
      Stop moving
      Grab the red block
      red_block_found = TRUE
  Navigate to red_dropoff_position at transport_speed
  Release the red block

// --- Collect Yellow Block ---
Function collect_yellow_block():
  While yellow_block_found is FALSE:
    Move forward at search_speed
    If ultrasonic sensor detects obstacle within obstacle_avoidance_distance:
      Perform obstacle_avoidance()
    If color sensor detects target color YELLOW:
      Stop moving
      Grab the yellow block
      yellow_block_found = TRUE
  Navigate to yellow_dropoff_position at transport_speed
  Release the yellow block

// --- Obstacle Avoidance ---
Function perform_obstacle_avoidance():
  Stop moving
  Move backward slightly
  Turn left or right randomly (small angle)
  Move forward briefly

// --- Navigation (Simplified) ---
Function navigate_to_position(target_position, speed):
  // This would involve more complex logic in a real implementation
  // For pseudocode, we'll keep it simple:
  Move towards target_position at speed
  // Assume some mechanism (e.g., time-based or encoder-based) to know when reached

// --- Main Execution ---
collect_red_block()
collect_yellow_block()

# SECOND PSEUDOCODE
// --- Initialization ---
Initialize EV3 sensors (color sensor, ultrasonic sensor, motor ports)
Define target color RED
Define target color YELLOW
Define red_dropoff_position
Define yellow_dropoff_position
Define search_speed
Define transport_speed
Define obstacle_avoidance_distance
Define search_pattern  // e.g., spiral, back and forth

// --- Main Program ---

// --- Search and Collect ---
Function search_and_collect():
  While red_block_collected is FALSE or yellow_block_collected is FALSE:
    Follow the defined search_pattern at search_speed
    If ultrasonic sensor detects obstacle within obstacle_avoidance_distance:
      Perform obstacle_avoidance()
    If color sensor detects target color RED and red_block_collected is FALSE:
      Stop moving
      Grab the red block
      red_block_collected = TRUE
      Navigate to red_dropoff_position at transport_speed
      Release the red block
      // Optionally, return to the search area
    Else If color sensor detects target color YELLOW and yellow_block_collected is FALSE:
      Stop moving
      Grab the yellow block
      yellow_block_collected = TRUE
      Navigate to yellow_dropoff_position at transport_speed
      Release the yellow block
      // Optionally, return to the search area

// --- Obstacle Avoidance ---
Function perform_obstacle_avoidance():
  Stop moving
  Move backward slightly
  Turn left or right randomly (small angle)
  Move forward briefly

// --- Navigation (Simplified) ---
Function navigate_to_position(target_position, speed):
  // ... (same as in Solution 1)

// --- Main Execution ---
search_and_collect()

# THIRD PSEUDOCODE
// --- Initialization ---
Initialize EV3 sensors (color sensor, ultrasonic sensor, motor ports)
Define target color RED
Define target color YELLOW
Define red_dropoff_position
Define yellow_dropoff_position
Define search_speed
Define transport_speed
Define obstacle_avoidance_distance
Define search_pattern

// --- Main Program ---

// --- Locate Blocks ---
Function locate_blocks():
  While red_block_location is UNKNOWN or yellow_block_location is UNKNOWN:
    Follow search_pattern at search_speed
    If ultrasonic sensor detects obstacle:
      Perform obstacle_avoidance()
    If color sensor detects target color RED and red_block_location is UNKNOWN:
      Record red_block_location (e.g., relative to starting point)
    Else If color sensor detects target color YELLOW and yellow_block_location is UNKNOWN:
      Record yellow_block_location

// --- Transport Blocks ---
Function transport_blocks():
  // Strategy for which block to pick up first (e.g., closer one)
  If red_block_location is KNOWN:
    Navigate to red_block_location at transport_speed
    Grab red block
    Navigate to red_dropoff_position at transport_speed
    Release red block
  If yellow_block_location is KNOWN:
    Navigate to yellow_block_location at transport_speed
    Grab yellow block
    Navigate to yellow_dropoff_position at transport_speed
    Release yellow block

// --- Obstacle Avoidance ---
Function perform_obstacle_avoidance():
  // ... (same as in previous solutions)

// --- Navigation (Advanced - Requires more complex implementation) ---
Function navigate_to_position(target_location, speed):
  // This would involve path planning based on recorded locations and sensor input
  // Potentially using encoder values and turning angles

// --- Main Execution ---
locate_blocks()
transport_blocks()
