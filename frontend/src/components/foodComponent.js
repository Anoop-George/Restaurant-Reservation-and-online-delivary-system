import React from "react";
import Grid from "@material-ui/core/Grid";
import Typography from "@material-ui/core/Typography";
import Box from "@material-ui/core/Box";
import { makeStyles } from "@material-ui/core/styles";

const useStyles = makeStyles({
  root_left: {
    display: "inline",
    fontSize: "20px",
    color: "#2a0d40",
    fontWeight: "bold",
  },
  root_right: {
    display: "inline",
    fontSize: "20px",
    color: "#8f7e47",
    float: "right",
    fontWeight: "bold",
  },
});

function FoodComponent() {
  const classes = useStyles();

  return (
    <div>
      <Grid
        container
        direction="row"
        justify="center"
        alignItems="center"
        spacing={2}
      >
        <Grid item xs={10} sm={5}>
          <Grid item style={{ marginTop: 10, borderBottom: "1px solid #e3d340" }}>
            <div>
              <span className={classes.root_left}>
                dfvffffffffffffffffffffffffffffff
              </span>
              <span className={classes.root_right}>444</span>
              <div style={{marginBottom:3}}>sosonbrjngj</div>
            </div>
          </Grid>
        </Grid>
       
      </Grid>
    </div>
  );
}

export default FoodComponent;
